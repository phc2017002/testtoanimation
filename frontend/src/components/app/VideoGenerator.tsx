"use client";

import React, { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { Loader2, Upload, Link as LinkIcon, FileText, CheckCircle, AlertCircle, Download, Play, Layout, Clock, Settings, Menu, X, Video, ChevronRight, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input, Textarea } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { api, type InputType, type Category, type JobStatus } from "@/lib/api";
import { cn } from "@/lib/utils";
import Link from "next/link";

export function VideoGenerator() {
  const searchParams = useSearchParams();
  const [inputType, setInputType] = useState<InputType>("text");
  const [category, setCategory] = useState<Category>("tech_system");
  const [content, setContent] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [currentJob, setCurrentJob] = useState<JobStatus | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // Initialize from URL params
  useEffect(() => {
    const promptParam = searchParams.get("prompt");
    const categoryParam = searchParams.get("category");

    if (promptParam) {
      setContent(promptParam);
      setInputType("text");
    }

    if (categoryParam && ["tech_system", "product_startup", "mathematical"].includes(categoryParam)) {
      setCategory(categoryParam as Category);
    }
  }, [searchParams]);

  // Poll for job status
  useEffect(() => {
    let interval: NodeJS.Timeout;

    if (currentJob && ["pending", "generating_code", "rendering"].includes(currentJob.status)) {
      interval = setInterval(async () => {
        try {
          const status = await api.getJobStatus(currentJob.job_id);
          setCurrentJob(status);

          if (status.status === "failed") {
            setError(status.error || "Job failed");
            setIsGenerating(false);
          } else if (status.status === "completed") {
            setIsGenerating(false);
          }
        } catch (e) {
          console.error("Polling error", e);
        }
      }, 2000);
    }

    return () => clearInterval(interval);
  }, [currentJob]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!content) return;

    setIsGenerating(true);
    setError(null);
    setCurrentJob(null);

    try {
      const job = await api.createVideo(content, inputType, category);
      setCurrentJob({
        job_id: job.job_id,
        status: "pending",
        progress: { percentage: 0, message: "Initializing system..." },
        created_at: new Date().toISOString()
      });
    } catch (e: any) {
      setError(e.message);
      setIsGenerating(false);
    }
  };

  const categories: { value: Category; label: string; description: string }[] = [
    { value: "tech_system", label: "Tech & Systems", description: "Architecture, Data Flow, APIs" },
    { value: "product_startup", label: "Product Demo", description: "Features, Value Prop, UI/UX" },
    { value: "mathematical", label: "Math & Research", description: "Equations, Graphs, Concepts" },
  ];

  return (
    <div className="flex h-screen bg-slate-950 overflow-hidden">
      {/* Mobile Sidebar Overlay */}
      <AnimatePresence>
        {isSidebarOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setIsSidebarOpen(false)}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 md:hidden"
          />
        )}
      </AnimatePresence>

      {/* Sidebar */}
      <motion.div
        className={cn(
          "fixed inset-y-0 left-0 z-50 w-72 bg-slate-900/50 backdrop-blur-xl border-r border-white/5 flex flex-col transition-transform duration-300 md:translate-x-0 md:static",
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        )}
      >
        <div className="p-6 border-b border-white/5 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-violet-600">
              <Video className="h-4 w-4 text-white" />
            </div>
            <span className="text-lg font-bold text-white">VidSimplify</span>
          </Link>
          <button onClick={() => setIsSidebarOpen(false)} className="md:hidden text-slate-400 hover:text-white">
            <X className="h-5 w-5" />
          </button>
        </div>

        <div className="flex-1 py-6 px-4 space-y-2 overflow-y-auto custom-scrollbar">
          <Button variant="ghost" className="w-full justify-start text-blue-400 bg-blue-500/10 hover:bg-blue-500/20 hover:text-blue-300 font-medium">
            <Layout className="mr-3 h-4 w-4" />
            Create New
          </Button>
          <Button variant="ghost" className="w-full justify-start text-slate-400 hover:text-white hover:bg-white/5">
            <Clock className="mr-3 h-4 w-4" />
            History
          </Button>
          <Button variant="ghost" className="w-full justify-start text-slate-400 hover:text-white hover:bg-white/5">
            <Settings className="mr-3 h-4 w-4" />
            Settings
          </Button>
        </div>

        <div className="p-4 border-t border-white/5 bg-slate-900/50">
          <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-xl p-4 border border-white/5">
            <div className="flex justify-between items-center mb-2">
              <div className="text-xs font-medium text-slate-300">Credits</div>
              <div className="text-xs font-mono text-blue-400">7/10</div>
            </div>
            <div className="h-1.5 bg-slate-700/50 rounded-full overflow-hidden mb-3">
              <div className="h-full bg-gradient-to-r from-blue-500 to-violet-500 w-[70%] rounded-full"></div>
            </div>
            <Button size="sm" variant="outline" className="w-full text-xs h-8 border-slate-700 hover:bg-slate-800 text-slate-300">
              Upgrade Plan
            </Button>
          </div>
        </div>
      </motion.div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden relative">
        {/* App Header */}
        <header className="h-16 border-b border-white/5 bg-slate-950/50 backdrop-blur-md flex items-center justify-between px-4 sm:px-8 z-30">
          <div className="flex items-center gap-4">
            <button onClick={() => setIsSidebarOpen(true)} className="md:hidden text-slate-400 hover:text-white p-1">
              <Menu className="h-6 w-6" />
            </button>
            <h1 className="text-lg font-semibold text-white flex items-center gap-2">
              <span className="text-slate-500 font-normal">Project /</span> Untitled Animation
            </h1>
          </div>
          <div className="flex items-center gap-4">
            <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full bg-green-500/10 border border-green-500/20 text-xs font-medium text-green-400">
              <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
              System Operational
            </div>
            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-500 to-violet-500 border border-white/20 shadow-lg" />
          </div>
        </header>

        <main className="flex-1 overflow-y-auto p-4 sm:p-8 custom-scrollbar">
          <div className="max-w-6xl mx-auto">
            <div className="grid lg:grid-cols-12 gap-8">

              {/* Left Column: Input Configuration */}
              <div className="lg:col-span-7 space-y-8">
                <div>
                  <h2 className="text-2xl font-bold text-white mb-2">Configure Generation</h2>
                  <p className="text-slate-400">Define the parameters for your AI-generated animation.</p>
                </div>

                <form onSubmit={handleSubmit} className="space-y-8">
                  {/* Input Source */}
                  <div className="space-y-4">
                    <label className="text-sm font-medium text-slate-300 uppercase tracking-wider">Input Source</label>
                    <div className="grid grid-cols-3 gap-4">
                      {[
                        { id: "text", icon: FileText, label: "Text Prompt" },
                        { id: "url", icon: LinkIcon, label: "URL / Blog" },
                        { id: "pdf", icon: Upload, label: "PDF Document" }
                      ].map((type) => (
                        <button
                          key={type.id}
                          type="button"
                          onClick={() => setInputType(type.id as InputType)}
                          className={cn(
                            "flex flex-col items-center justify-center p-4 rounded-xl border transition-all duration-200",
                            inputType === type.id
                              ? "bg-blue-600/10 border-blue-500/50 text-blue-400 shadow-[0_0_20px_rgba(59,130,246,0.15)]"
                              : "bg-slate-900/50 border-white/5 text-slate-400 hover:bg-slate-800 hover:border-white/10"
                          )}
                        >
                          <type.icon className="w-6 h-6 mb-2" />
                          <span className="text-sm font-medium">{type.label}</span>
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Animation Style */}
                  <div className="space-y-4">
                    <label className="text-sm font-medium text-slate-300 uppercase tracking-wider">Visual Style</label>
                    <div className="grid gap-3">
                      {categories.map((cat) => (
                        <button
                          key={cat.value}
                          type="button"
                          onClick={() => setCategory(cat.value)}
                          className={cn(
                            "flex items-center p-4 rounded-xl border text-left transition-all duration-200",
                            category === cat.value
                              ? "bg-violet-600/10 border-violet-500/50 shadow-[0_0_20px_rgba(139,92,246,0.15)]"
                              : "bg-slate-900/50 border-white/5 hover:bg-slate-800 hover:border-white/10"
                          )}
                        >
                          <div className={cn(
                            "w-10 h-10 rounded-lg flex items-center justify-center mr-4 transition-colors",
                            category === cat.value ? "bg-violet-500/20 text-violet-400" : "bg-slate-800 text-slate-400"
                          )}>
                            {cat.value === 'tech_system' && <Layout className="w-5 h-5" />}
                            {cat.value === 'product_startup' && <Sparkles className="w-5 h-5" />}
                            {cat.value === 'mathematical' && <Clock className="w-5 h-5" />}
                          </div>
                          <div>
                            <div className={cn("font-medium", category === cat.value ? "text-violet-300" : "text-slate-200")}>
                              {cat.label}
                            </div>
                            <div className="text-xs text-slate-500 mt-0.5">{cat.description}</div>
                          </div>
                          {category === cat.value && (
                            <div className="ml-auto text-violet-400">
                              <CheckCircle className="w-5 h-5" />
                            </div>
                          )}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Content Input */}
                  <div className="space-y-4">
                    <label className="text-sm font-medium text-slate-300 uppercase tracking-wider">
                      {inputType === "text" ? "Description" : inputType === "url" ? "Source URL" : "Upload File"}
                    </label>

                    <div className="relative group">
                      <div className="absolute -inset-0.5 bg-gradient-to-r from-blue-500 to-violet-500 rounded-xl opacity-0 group-hover:opacity-20 transition duration-500 blur"></div>
                      {inputType === "text" ? (
                        <Textarea
                          placeholder="Explain the concept of neural networks using a simple analogy..."
                          className="relative min-h-[200px] text-base resize-none bg-slate-900/80 border-white/10 text-slate-200 focus:border-blue-500/50 focus:ring-blue-500/20 rounded-xl p-4"
                          value={content}
                          onChange={(e) => setContent(e.target.value)}
                        />
                      ) : inputType === "url" ? (
                        <Input
                          placeholder="https://example.com/article"
                          value={content}
                          onChange={(e) => setContent(e.target.value)}
                          className="relative h-12 bg-slate-900/80 border-white/10 text-slate-200 focus:border-blue-500/50 focus:ring-blue-500/20 rounded-xl px-4"
                        />
                      ) : (
                        <div className="relative border-2 border-dashed border-slate-700 rounded-xl p-12 text-center hover:border-blue-500/50 hover:bg-slate-900/50 transition-all cursor-pointer">
                          <Input
                            type="file"
                            accept=".pdf"
                            onChange={async (e) => {
                              const file = e.target.files?.[0];
                              if (file) {
                                const reader = new FileReader();
                                reader.onload = (event) => {
                                  const base64 = event.target?.result as string;
                                  const base64Content = base64.split(',')[1];
                                  setContent(base64Content);
                                };
                                reader.readAsDataURL(file);
                              }
                            }}
                            className="hidden"
                            id="pdf-upload"
                          />
                          <label htmlFor="pdf-upload" className="cursor-pointer w-full h-full block">
                            <div className="w-16 h-16 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                              <Upload className="h-8 w-8 text-slate-400 group-hover:text-blue-400 transition-colors" />
                            </div>
                            <p className="text-lg font-medium text-slate-300 mb-2">Click to upload PDF</p>
                            <p className="text-sm text-slate-500">Maximum file size 10MB</p>
                          </label>
                          {content && (
                            <div className="absolute top-4 right-4 flex items-center gap-2 text-green-400 text-xs bg-green-500/10 py-1.5 px-3 rounded-full border border-green-500/20">
                              <CheckCircle className="h-3 w-3" />
                              <span>Ready</span>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  </div>

                  <Button
                    type="submit"
                    size="lg"
                    className="w-full h-16 text-lg font-semibold bg-gradient-to-r from-blue-600 to-violet-600 hover:from-blue-500 hover:to-violet-500 text-white shadow-lg shadow-blue-500/25 rounded-xl transition-all hover:scale-[1.02] active:scale-[0.98]"
                    disabled={isGenerating || !content}
                  >
                    {isGenerating ? (
                      <div className="flex items-center gap-3">
                        <Loader2 className="h-6 w-6 animate-spin" />
                        <span>Processing Request...</span>
                      </div>
                    ) : (
                      <div className="flex items-center gap-3">
                        <Play className="h-6 w-6 fill-current" />
                        <span>Generate Animation</span>
                      </div>
                    )}
                  </Button>
                </form>
              </div>

              {/* Right Column: Preview & Status */}
              <div className="lg:col-span-5 space-y-8">
                <div>
                  <h2 className="text-2xl font-bold text-white mb-2">Live Preview</h2>
                  <p className="text-slate-400">Real-time generation status and output.</p>
                </div>

                <div className="sticky top-8">
                  <AnimatePresence mode="wait">
                    {currentJob ? (
                      <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -20 }}
                        className="space-y-6"
                      >
                        <Card className="bg-slate-900 border-white/10 overflow-hidden shadow-2xl">
                          <CardHeader className="border-b border-white/5 bg-slate-950/30 py-4">
                            <div className="flex items-center justify-between">
                              <CardTitle className="text-sm font-medium text-slate-300 flex items-center gap-2">
                                {currentJob.status === "completed" ? (
                                  <span className="flex items-center gap-2 text-green-400">
                                    <CheckCircle className="h-4 w-4" /> Completed
                                  </span>
                                ) : currentJob.status === "failed" ? (
                                  <span className="flex items-center gap-2 text-red-400">
                                    <AlertCircle className="h-4 w-4" /> Failed
                                  </span>
                                ) : (
                                  <span className="flex items-center gap-2 text-blue-400">
                                    <Loader2 className="h-4 w-4 animate-spin" /> Processing
                                  </span>
                                )}
                              </CardTitle>
                              <div className="text-xs font-mono text-slate-500">{currentJob.job_id.slice(0, 8)}</div>
                            </div>
                          </CardHeader>

                          <CardContent className="p-0">
                            {/* Video Player or Progress State */}
                            <div className="aspect-video bg-black relative group">
                              {currentJob.status === "completed" ? (
                                <video
                                  src={api.getVideoUrl(currentJob.job_id)}
                                  controls
                                  className="w-full h-full"
                                  poster="/placeholder-video.jpg"
                                />
                              ) : (
                                <div className="absolute inset-0 flex flex-col items-center justify-center p-8 text-center">
                                  <div className="relative w-24 h-24 mb-6">
                                    <div className="absolute inset-0 rounded-full border-4 border-slate-800"></div>
                                    <div className="absolute inset-0 rounded-full border-4 border-t-blue-500 border-r-transparent border-b-transparent border-l-transparent animate-spin"></div>
                                    <div className="absolute inset-4 rounded-full bg-slate-800/50 backdrop-blur flex items-center justify-center">
                                      <span className="text-sm font-bold text-white">{currentJob.progress.percentage}%</span>
                                    </div>
                                  </div>
                                  <h3 className="text-lg font-medium text-white mb-2">Generating Animation</h3>
                                  <p className="text-sm text-slate-400 max-w-xs mx-auto animate-pulse">
                                    {currentJob.progress.message}
                                  </p>
                                </div>
                              )}
                            </div>

                            {/* Actions */}
                            {currentJob.status === "completed" && (
                              <div className="p-4 bg-slate-900 border-t border-white/5">
                                <Button className="w-full bg-white text-slate-900 hover:bg-slate-200 font-medium" asChild>
                                  <a href={api.getVideoUrl(currentJob.job_id)} download>
                                    <Download className="mr-2 h-4 w-4" />
                                    Download MP4 (1080p)
                                  </a>
                                </Button>
                              </div>
                            )}

                            {/* Error Message */}
                            {error && (
                              <div className="p-4 bg-red-500/10 border-t border-red-500/20">
                                <p className="text-sm text-red-400 flex items-start gap-2">
                                  <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
                                  {error}
                                </p>
                              </div>
                            )}
                          </CardContent>
                        </Card>

                        {/* Process Steps (Visual Decoration) */}
                        {currentJob.status !== "completed" && currentJob.status !== "failed" && (
                          <div className="space-y-3">
                            {["Analyzing Input", "Generating Script", "Validating Code", "Rendering Frames"].map((step, i) => {
                              const currentStepIndex = Math.floor((currentJob.progress.percentage / 100) * 4);
                              const isActive = i === currentStepIndex;
                              const isCompleted = i < currentStepIndex;

                              return (
                                <div key={step} className="flex items-center gap-3 text-sm">
                                  <div className={cn(
                                    "w-6 h-6 rounded-full flex items-center justify-center border transition-colors",
                                    isCompleted ? "bg-green-500 border-green-500 text-slate-900" :
                                      isActive ? "border-blue-500 text-blue-500" : "border-slate-700 text-slate-700"
                                  )}>
                                    {isCompleted ? <CheckCircle className="w-4 h-4" /> : <div className={cn("w-2 h-2 rounded-full", isActive ? "bg-blue-500 animate-pulse" : "bg-slate-700")} />}
                                  </div>
                                  <span className={cn(
                                    "transition-colors",
                                    isCompleted ? "text-slate-300" :
                                      isActive ? "text-white font-medium" : "text-slate-600"
                                  )}>{step}</span>
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </motion.div>
                    ) : (
                      <div className="h-[400px] rounded-2xl border-2 border-dashed border-slate-800 bg-slate-900/30 flex flex-col items-center justify-center text-slate-500 p-8 text-center">
                        <div className="w-20 h-20 rounded-full bg-slate-800/50 flex items-center justify-center mb-6">
                          <Video className="h-10 w-10 opacity-50" />
                        </div>
                        <h3 className="text-lg font-medium text-slate-300 mb-2">Ready to Generate</h3>
                        <p className="max-w-xs text-sm">
                          Configure your animation parameters on the left and click generate to see the magic happen.
                        </p>
                      </div>
                    )}
                  </AnimatePresence>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
