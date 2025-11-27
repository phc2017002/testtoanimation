"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, Code2, Database, BrainCircuit, Rocket, ArrowRight, Check } from "lucide-react";
import { Button } from "@/components/ui/button";
import Link from "next/link";

type Category = "tech" | "research" | "product";

interface DemoPrompt {
    id: string;
    category: Category;
    title: string;
    prompt: string;
    duration: string;
    icon: React.ReactNode;
}

const DEMO_PROMPTS: DemoPrompt[] = [
    {
        id: "sharding",
        category: "tech",
        title: "Database Sharding",
        prompt: "Create a 4 min video explaining the concept of database sharding in system design. Show how data is distributed across multiple nodes to handle high traffic.",
        duration: "4:00",
        icon: <Database className="h-6 w-6 text-blue-400" />
    },
    {
        id: "kafka",
        category: "tech",
        title: "Apache Kafka",
        prompt: "Explain the working of kafka in entire detail in 5 mins. Cover topics, partitions, producers, consumers, and consumer groups.",
        duration: "5:00",
        icon: <Code2 className="h-6 w-6 text-green-400" />
    },
    {
        id: "transformers",
        category: "research",
        title: "Transformers Architecture",
        prompt: "Explain the research paper 'Attention is all you need: Transformers' in detail. Visualize the encoder-decoder structure and self-attention mechanism.",
        duration: "6:30",
        icon: <BrainCircuit className="h-6 w-6 text-purple-400" />
    },
    {
        id: "quantum",
        category: "research",
        title: "Quantum Entanglement",
        prompt: "Explain the concept of quantum entanglement. Visualize two particles sharing a state regardless of distance.",
        duration: "3:45",
        icon: <BrainCircuit className="h-6 w-6 text-violet-400" />
    },
    {
        id: "netflix",
        category: "product",
        title: "Netflix Business Model",
        prompt: "Explain the business model of netflix in detail in 5 mins. Cover subscription tiers, content acquisition, and recommendation algorithms.",
        duration: "5:00",
        icon: <Rocket className="h-6 w-6 text-orange-400" />
    },
    {
        id: "blackhole",
        category: "research",
        title: "Black Hole Physics",
        prompt: "Explain the event horizon and singularity of a black hole. Visualize light bending due to extreme gravity.",
        duration: "4:15",
        icon: <BrainCircuit className="h-6 w-6 text-indigo-400" />
    },
    {
        id: "sorting",
        category: "tech",
        title: "Sorting Algorithms",
        prompt: "Visualize how QuickSort works compared to Bubble Sort. Show the step-by-step element swapping process.",
        duration: "3:30",
        icon: <Code2 className="h-6 w-6 text-emerald-400" />
    },
    {
        id: "uber",
        category: "product",
        title: "Uber System Design",
        prompt: "Explain the high-level architecture of Uber. Cover driver matching, location tracking, and payment processing.",
        duration: "5:45",
        icon: <Rocket className="h-6 w-6 text-pink-400" />
    }
];

export function Showcase() {
    const [activeCategory, setActiveCategory] = useState<Category | "all">("all");
    const [selectedPrompt, setSelectedPrompt] = useState<DemoPrompt | null>(DEMO_PROMPTS[0]);
    const [showAll, setShowAll] = useState(false);

    const filteredPrompts = activeCategory === "all"
        ? DEMO_PROMPTS
        : DEMO_PROMPTS.filter(p => p.category === activeCategory);

    return (
        <section id="showcase" className="py-24 bg-slate-950 relative overflow-hidden">
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-px bg-gradient-to-r from-transparent via-blue-500/50 to-transparent" />

            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative z-10">
                <div className="text-center mb-12">
                    <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl mb-4">
                        See What You Can Build
                    </h2>
                    <p className="text-lg text-slate-400 max-w-2xl mx-auto">
                        Select a prompt to see how VidSimplify transforms simple text into complex, precise animations.
                    </p>
                </div>

                {/* Category Filter */}
                <div className="flex justify-center gap-4 mb-8 flex-wrap">
                    {[
                        { id: "all", label: "All Examples" },
                        { id: "tech", label: "Tech & Systems" },
                        { id: "research", label: "Research & Math" },
                        { id: "product", label: "Product & Startups" }
                    ].map((cat) => (
                        <button
                            key={cat.id}
                            onClick={() => {
                                setActiveCategory(cat.id as any);
                                const newPrompts = cat.id === "all"
                                    ? DEMO_PROMPTS
                                    : DEMO_PROMPTS.filter(p => p.category === cat.id);
                                setSelectedPrompt(newPrompts[0] || null);
                            }}
                            className={`px-6 py-2 rounded-full text-sm font-medium transition-all ${activeCategory === cat.id
                                ? "bg-blue-600 text-white shadow-lg shadow-blue-500/25"
                                : "bg-slate-900 text-slate-400 hover:bg-slate-800 hover:text-white border border-slate-800"
                                }`}
                        >
                            {cat.label}
                        </button>
                    ))}
                </div>

                <div className="flex flex-col gap-8">
                    {/* Large Preview Area */}
                    <div className="w-full aspect-video lg:aspect-[21/9] bg-slate-900 rounded-2xl border border-white/10 overflow-hidden shadow-2xl relative group">
                        {selectedPrompt ? (
                            <>
                                {/* Mock Video Player */}
                                <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-slate-800 flex items-center justify-center">
                                    <div className="text-center p-8">
                                        <div className="w-24 h-24 bg-blue-600/20 rounded-full flex items-center justify-center mx-auto mb-6 animate-pulse">
                                            <Play className="h-10 w-10 text-blue-400 ml-1" />
                                        </div>
                                        <h3 className="text-3xl font-bold text-white mb-2">
                                            {selectedPrompt.title}
                                        </h3>
                                        <p className="text-slate-400 mb-8 text-lg">
                                            Preview of generated animation
                                        </p>

                                        <Link href={`/app?prompt=${encodeURIComponent(selectedPrompt.prompt)}&category=${selectedPrompt.category === 'tech' ? 'tech_system' : selectedPrompt.category === 'research' ? 'mathematical' : 'product_startup'}`}>
                                            <Button size="lg" className="h-14 px-8 text-lg bg-blue-600 hover:bg-blue-500 text-white">
                                                Generate This Video <ArrowRight className="ml-2 h-5 w-5" />
                                            </Button>
                                        </Link>
                                    </div>
                                </div>

                                {/* Overlay Info */}
                                <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-slate-950 to-transparent p-8 pt-24">
                                    <div className="flex gap-6 text-sm text-slate-300">
                                        <div className="flex items-center gap-2">
                                            <Check className="h-4 w-4 text-green-400" />
                                            Script Generated
                                        </div>
                                        <div className="flex items-center gap-2">
                                            <Check className="h-4 w-4 text-green-400" />
                                            Code Validated
                                        </div>
                                        <div className="flex items-center gap-2">
                                            <Check className="h-4 w-4 text-green-400" />
                                            Voiceover Synced
                                        </div>
                                    </div>
                                </div>
                            </>
                        ) : (
                            <div className="absolute inset-0 flex items-center justify-center text-slate-500">
                                <div className="text-center">
                                    <Play className="h-16 w-16 mx-auto mb-4 opacity-20" />
                                    <p className="text-xl">Select a prompt below to preview</p>
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Horizontal Slider for Prompts */}
                    <div className="w-full overflow-x-auto pb-4 custom-scrollbar">
                        <div className="flex gap-4 min-w-max px-2">
                            <AnimatePresence mode="popLayout">
                                {filteredPrompts.map((prompt) => (
                                    <motion.div
                                        key={prompt.id}
                                        layout
                                        initial={{ opacity: 0, scale: 0.9 }}
                                        animate={{ opacity: 1, scale: 1 }}
                                        exit={{ opacity: 0, scale: 0.9 }}
                                        onClick={() => setSelectedPrompt(prompt)}
                                        className={`w-80 p-5 rounded-xl border cursor-pointer transition-all group flex-shrink-0 ${selectedPrompt?.id === prompt.id
                                            ? "bg-blue-900/20 border-blue-500/50 shadow-lg shadow-blue-900/20"
                                            : "bg-slate-900/50 border-white/5 hover:bg-slate-800/50 hover:border-white/10"
                                            }`}
                                    >
                                        <div className="flex flex-col h-full">
                                            <div className="flex items-center gap-3 mb-3">
                                                <div className={`p-2 rounded-lg ${selectedPrompt?.id === prompt.id ? "bg-blue-500/20" : "bg-slate-800"
                                                    }`}>
                                                    {prompt.icon}
                                                </div>
                                                <div className="flex-1 min-w-0">
                                                    <h3 className={`font-semibold truncate ${selectedPrompt?.id === prompt.id ? "text-blue-400" : "text-white"
                                                        }`}>
                                                        {prompt.title}
                                                    </h3>
                                                    <span className="text-xs text-slate-500">
                                                        {prompt.duration}
                                                    </span>
                                                </div>
                                            </div>
                                            <p className="text-sm text-slate-400 line-clamp-2 group-hover:text-slate-300 transition-colors mb-3 flex-1">
                                                "{prompt.prompt}"
                                            </p>
                                            <div className={`flex items-center text-xs font-medium ${selectedPrompt?.id === prompt.id ? "text-blue-400 opacity-100" : "text-slate-500 opacity-0 group-hover:opacity-100"
                                                } transition-all`}>
                                                Preview <ArrowRight className="ml-1 h-3 w-3" />
                                            </div>
                                        </div>
                                    </motion.div>
                                ))}
                            </AnimatePresence>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
