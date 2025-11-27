"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { ArrowRight, Terminal, Activity, Zap, Layers, Share2, Cpu, Play, Sparkles } from "lucide-react";

const EXAMPLES = [
    {
        prompt: "Visualize a Binary Search Tree",
        process: "Structuring Logic...",
        visual: (
            <svg viewBox="0 0 100 100" className="w-full h-full text-violet-400">
                <motion.circle cx="50" cy="20" r="5" fill="currentColor" initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ duration: 0.3 }} />
                <motion.path d="M50 20 L30 50" stroke="currentColor" strokeWidth="2" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3, delay: 0.2 }} />
                <motion.path d="M50 20 L70 50" stroke="currentColor" strokeWidth="2" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3, delay: 0.2 }} />
                <motion.circle cx="30" cy="50" r="5" fill="currentColor" initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ duration: 0.3, delay: 0.4 }} />
                <motion.circle cx="70" cy="50" r="5" fill="currentColor" initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ duration: 0.3, delay: 0.4 }} />
                <motion.path d="M30 50 L20 80" stroke="currentColor" strokeWidth="2" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3, delay: 0.6 }} />
                <motion.path d="M30 50 L40 80" stroke="currentColor" strokeWidth="2" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3, delay: 0.6 }} />
                <motion.circle cx="20" cy="80" r="5" fill="currentColor" initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ duration: 0.3, delay: 0.8 }} />
                <motion.circle cx="40" cy="80" r="5" fill="currentColor" initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ duration: 0.3, delay: 0.8 }} />
            </svg>
        )
    },
    {
        prompt: "Explain Solar System Orbits",
        process: "Calculating Trajectories...",
        visual: (
            <svg viewBox="0 0 100 100" className="w-full h-full">
                <circle cx="50" cy="50" r="8" fill="#fbbf24" />
                <motion.g animate={{ rotate: 360 }} transition={{ duration: 4, repeat: Infinity, ease: "linear" }}>
                    <circle cx="50" cy="50" r="25" stroke="#4b5563" strokeWidth="1" fill="none" />
                    <circle cx="75" cy="50" r="4" fill="#3b82f6" />
                </motion.g>
                <motion.g animate={{ rotate: 360 }} transition={{ duration: 6, repeat: Infinity, ease: "linear" }}>
                    <circle cx="50" cy="50" r="40" stroke="#4b5563" strokeWidth="1" fill="none" />
                    <circle cx="90" cy="50" r="3" fill="#ef4444" />
                </motion.g>
            </svg>
        )
    },
    {
        prompt: "Neural Network Architecture",
        process: "Connecting Layers...",
        visual: (
            <svg viewBox="0 0 100 100" className="w-full h-full text-indigo-400">
                {[20, 50, 80].map((x, i) => (
                    <g key={x}>
                        {[20, 50, 80].map((y, j) => (
                            <motion.circle
                                key={`${x}-${y}`}
                                cx={x}
                                cy={y}
                                r="3"
                                fill="currentColor"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: i * 0.2 + j * 0.1 }}
                            />
                        ))}
                    </g>
                ))}
                <motion.path
                    d="M20 20 L50 50 M20 50 L50 50 M20 80 L50 50 M50 50 L80 20 M50 50 L80 50 M50 50 L80 80"
                    stroke="currentColor"
                    strokeWidth="0.5"
                    strokeOpacity="0.5"
                    initial={{ pathLength: 0 }}
                    animate={{ pathLength: 1 }}
                    transition={{ duration: 1, delay: 0.5 }}
                />
            </svg>
        )
    }
];

export function Hero() {
    const [activeExample, setActiveExample] = useState(0);
    const [step, setStep] = useState(0); // 0: Input, 1: Process, 2: Output

    useEffect(() => {
        const timer = setInterval(() => {
            setStep(prev => {
                if (prev === 2) {
                    setActiveExample(current => (current + 1) % EXAMPLES.length);
                    return 0;
                }
                return prev + 1;
            });
        }, 2500); // Change step every 2.5s

        return () => clearInterval(timer);
    }, []);

    return (
        <div className="relative overflow-hidden bg-slate-950 pt-20 pb-32 lg:pt-32 lg:pb-40">
            {/* Background Effects */}
            <div className="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))]" />
            <div className="absolute top-0 right-0 -translate-y-12 translate-x-12 blur-3xl opacity-20">
                <div className="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30" />
            </div>
            <div className="absolute bottom-0 left-0 translate-y-12 -translate-x-12 blur-3xl opacity-20">
                <div className="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#4f46e5] to-[#80caff] opacity-30" />
            </div>

            <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="grid lg:grid-cols-2 gap-16 items-center">
                    <div className="text-left">
                        <div className="inline-flex items-center rounded-full border border-blue-500/30 bg-blue-500/10 px-3 py-1 text-sm font-medium text-blue-400 mb-8 backdrop-blur-sm">
                            <span className="flex h-2 w-2 rounded-full bg-blue-400 mr-2 animate-pulse"></span>
                            Vidsimplify 1.0 Launch
                        </div>

                        <h1 className="text-4xl font-bold tracking-tight text-white sm:text-7xl mb-6 leading-tight">
                            Precision Animation is <br />
                            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-violet-400 to-indigo-400">
                                Future.
                            </span>
                        </h1>

                        <div className="space-y-6 text-lg text-slate-400 mb-8 leading-relaxed max-w-xl">
                            <p>
                                The random AI video generation is inaccurate, hallucinated, inexplainable and can't be edited.
                            </p>
                            <p>
                                In the growing complex world we need <span className="text-blue-400 font-semibold">precision animation</span>. Simply type a prompt, and VidSimplify generates a mathematically accurate video explaining your system, research, or product in depth.
                            </p>
                            <p className="text-slate-300 font-medium border-l-2 border-blue-500 pl-4">
                                We are here to change the game of video explanations.
                            </p>
                        </div>

                        <div className="flex flex-col sm:flex-row gap-4 mb-12">
                            <Link href="/app">
                                <Button size="lg" className="h-14 px-8 text-lg bg-blue-600 hover:bg-blue-500 text-white border-0 shadow-lg shadow-blue-500/25 w-full sm:w-auto transition-all hover:scale-105">
                                    Start Creating <ArrowRight className="ml-2 h-5 w-5" />
                                </Button>
                            </Link>
                            <Link href="/api-docs">
                                <Button variant="outline" size="lg" className="h-14 px-8 text-lg border-slate-700 text-slate-300 hover:bg-slate-800 hover:text-white w-full sm:w-auto">
                                    <Activity className="mr-2 h-5 w-5" />
                                    How it Works
                                </Button>
                            </Link>
                        </div>

                        <div className="flex items-center gap-8 text-slate-500 text-sm font-medium">
                            <div className="flex items-center gap-2">
                                <Cpu className="h-4 w-4 text-blue-500" />
                                <span>Tech & Systems</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <Layers className="h-4 w-4 text-violet-500" />
                                <span>Research & Math</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <Share2 className="h-4 w-4 text-indigo-500" />
                                <span>Product Demos</span>
                            </div>
                        </div>
                    </div>

                    {/* Hero Visual - Interactive Pipeline */}
                    <div className="relative lg:h-[600px] w-full hidden lg:block">
                        <div className="absolute inset-0 bg-gradient-to-tr from-blue-500/10 to-violet-500/10 rounded-2xl border border-white/10 backdrop-blur-sm p-4">
                            <div className="h-full w-full bg-slate-900/90 rounded-xl overflow-hidden relative group flex flex-col items-center justify-center">

                                {/* Top Bar: System Status */}
                                <div className="absolute top-0 left-0 right-0 h-12 border-b border-white/5 bg-slate-950/50 backdrop-blur flex items-center justify-between px-4 z-20">
                                    <div className="flex gap-2">
                                        <div className="w-3 h-3 rounded-full bg-red-500/20 border border-red-500/50" />
                                        <div className="w-3 h-3 rounded-full bg-yellow-500/20 border border-yellow-500/50" />
                                        <div className="w-3 h-3 rounded-full bg-green-500/20 border border-green-500/50" />
                                    </div>
                                    <div className="flex items-center gap-4">
                                        <div className="flex items-center gap-2 text-[10px] font-mono text-slate-500">
                                            <Activity className="h-3 w-3" />
                                            <span>SYSTEM_READY</span>
                                        </div>
                                        <div className="flex items-center gap-2 text-[10px] font-mono text-blue-500/70">
                                            <Cpu className="h-3 w-3" />
                                            <span>MATH_CORE_ACTIVE</span>
                                        </div>
                                    </div>
                                </div>

                                {/* Pipeline Container */}
                                <div className="w-full max-w-lg relative z-10 py-12">

                                    {/* Connecting Lines Background */}
                                    <div className="absolute top-1/2 left-0 w-full h-1 bg-slate-800 -translate-y-1/2 rounded-full overflow-hidden">
                                        <motion.div
                                            className="h-full bg-gradient-to-r from-blue-500 to-violet-500"
                                            initial={{ x: "-100%" }}
                                            animate={{ x: step === 0 ? "-50%" : step === 1 ? "0%" : "100%" }}
                                            transition={{ duration: 1, ease: "easeInOut" }}
                                        />
                                    </div>

                                    <div className="flex justify-between items-center relative z-10">

                                        {/* Step 1: Input */}
                                        <motion.div
                                            className={`w-32 h-32 rounded-xl border-2 flex flex-col items-center justify-center p-4 bg-slate-900 transition-colors ${step === 0 ? 'border-blue-500 shadow-[0_0_20px_rgba(59,130,246,0.3)]' : 'border-slate-700'}`}
                                            animate={{ scale: step === 0 ? 1.05 : 1 }}
                                        >
                                            <Terminal className={`h-8 w-8 mb-3 ${step === 0 ? 'text-blue-400' : 'text-slate-500'}`} />
                                            <div className="text-xs text-center font-mono text-slate-300">
                                                <AnimatePresence mode="wait">
                                                    <motion.span
                                                        key={activeExample}
                                                        initial={{ opacity: 0 }}
                                                        animate={{ opacity: 1 }}
                                                        exit={{ opacity: 0 }}
                                                    >
                                                        "{EXAMPLES[activeExample].prompt}"
                                                    </motion.span>
                                                </AnimatePresence>
                                            </div>
                                        </motion.div>

                                        {/* Step 2: Processing */}
                                        <motion.div
                                            className={`w-32 h-32 rounded-full border-2 flex flex-col items-center justify-center bg-slate-900 transition-colors ${step === 1 ? 'border-violet-500 shadow-[0_0_20px_rgba(139,92,246,0.3)]' : 'border-slate-700'}`}
                                            animate={{
                                                scale: step === 1 ? 1.1 : 1,
                                                rotate: step === 1 ? 360 : 0
                                            }}
                                            transition={{ rotate: { duration: 2, repeat: step === 1 ? Infinity : 0, ease: "linear" } }}
                                        >
                                            <Zap className={`h-10 w-10 ${step === 1 ? 'text-violet-400' : 'text-slate-500'}`} />
                                        </motion.div>

                                        {/* Step 3: Output */}
                                        <motion.div
                                            className={`w-32 h-32 rounded-xl border-2 flex flex-col items-center justify-center bg-slate-900 overflow-hidden relative transition-colors ${step === 2 ? 'border-indigo-500 shadow-[0_0_20px_rgba(99,102,241,0.3)]' : 'border-slate-700'}`}
                                            animate={{ scale: step === 2 ? 1.05 : 1 }}
                                        >
                                            {step === 2 ? (
                                                <div className="w-full h-full p-2">
                                                    {EXAMPLES[activeExample].visual}
                                                </div>
                                            ) : (
                                                <Play className="h-8 w-8 text-slate-500" />
                                            )}
                                        </motion.div>
                                    </div>

                                    {/* Labels */}
                                    <div className="flex justify-between mt-4 text-xs font-medium text-slate-500 uppercase tracking-wider">
                                        <div className={`w-32 text-center transition-colors ${step === 0 ? 'text-blue-400' : ''}`}>Prompt</div>
                                        <div className={`w-32 text-center transition-colors ${step === 1 ? 'text-violet-400' : ''}`}>Logic Core</div>
                                        <div className={`w-32 text-center transition-colors ${step === 2 ? 'text-indigo-400' : ''}`}>Animation</div>
                                    </div>
                                </div>

                                {/* Dynamic Status Message */}
                                <motion.div
                                    className="mt-8 px-6 py-2 rounded-full bg-slate-800/50 border border-white/10 backdrop-blur-sm text-sm text-slate-300 flex items-center gap-2 z-10"
                                    key={step}
                                    initial={{ y: 20, opacity: 0 }}
                                    animate={{ y: 0, opacity: 1 }}
                                >
                                    {step === 0 && <Terminal className="h-4 w-4 text-blue-400" />}
                                    {step === 1 && <Sparkles className="h-4 w-4 text-violet-400" />}
                                    {step === 2 && <Play className="h-4 w-4 text-indigo-400" />}

                                    {step === 0 && "Waiting for input..."}
                                    {step === 1 && EXAMPLES[activeExample].process}
                                    {step === 2 && "Rendering final output"}
                                </motion.div>

                                {/* Bottom Bar: Live Logs */}
                                <div className="absolute bottom-0 left-0 right-0 h-32 border-t border-white/5 bg-slate-950/50 backdrop-blur p-4 font-mono text-[10px] text-slate-500 overflow-hidden z-20">
                                    <div className="flex justify-between items-center mb-2 border-b border-white/5 pb-1">
                                        <span>LIVE_EXECUTION_LOG</span>
                                        <span className="flex items-center gap-1"><span className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" /> ONLINE</span>
                                    </div>
                                    <div className="space-y-1">
                                        <AnimatePresence mode="popLayout">
                                            {step === 0 && (
                                                <>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} className="text-blue-400/80">&gt; DETECTED_INPUT_STREAM</motion.div>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.2 }}> &gt; ANALYZING_SEMANTICS...</motion.div>
                                                </>
                                            )}
                                            {step === 1 && (
                                                <>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} className="text-violet-400/80">&gt; GENERATING_MATHEMATICAL_MODELS</motion.div>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.2 }}> &gt; OPTIMIZING_GEOMETRY_NODES...</motion.div>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.4 }}> &gt; SOLVING_PHYSICS_CONSTRAINTS...</motion.div>
                                                </>
                                            )}
                                            {step === 2 && (
                                                <>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} className="text-indigo-400/80">&gt; RENDERING_FRAME_BUFFER</motion.div>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.2 }}> &gt; APPLYING_POST_PROCESSING...</motion.div>
                                                    <motion.div initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.4 }} className="text-green-400"> &gt; OUTPUT_GENERATED_SUCCESSFULLY</motion.div>
                                                </>
                                            )}
                                        </AnimatePresence>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
