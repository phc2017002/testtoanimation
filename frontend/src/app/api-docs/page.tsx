"use client";

import { Navbar } from "@/components/landing/Navbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Check, Copy, Terminal, Play, BarChart3, Coins } from "lucide-react";

export default function ApiDocs() {
    return (
        <main className="min-h-screen bg-slate-950">
            <Navbar />

            <div className="pt-24 pb-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
                <div className="text-center mb-16">
                    <h1 className="text-4xl font-bold text-white mb-4">VidSimplify API</h1>
                    <p className="text-xl text-slate-400 max-w-2xl mx-auto">
                        Integrate precision animation generation directly into your product.
                        Simple, RESTful, and scalable.
                    </p>
                </div>

                <div className="grid lg:grid-cols-3 gap-8">
                    {/* Main Documentation Area */}
                    <div className="lg:col-span-2 space-y-8">
                        <Card className="bg-slate-900 border-slate-800">
                            <CardHeader>
                                <CardTitle className="text-white flex items-center gap-2">
                                    <Terminal className="h-5 w-5 text-blue-400" />
                                    Quick Start
                                </CardTitle>
                                <CardDescription className="text-slate-400">
                                    Generate your first video in 3 steps
                                </CardDescription>
                            </CardHeader>
                            <CardContent>
                                <Tabs defaultValue="python" className="w-full">
                                    <TabsList className="bg-slate-950 border border-slate-800 mb-4">
                                        <TabsTrigger value="python">Python</TabsTrigger>
                                        <TabsTrigger value="curl">cURL</TabsTrigger>
                                        <TabsTrigger value="node">Node.js</TabsTrigger>
                                    </TabsList>

                                    <TabsContent value="python" className="space-y-4">
                                        <div className="bg-slate-950 p-4 rounded-lg border border-slate-800 font-mono text-sm text-slate-300 overflow-x-auto">
                                            <div className="flex justify-between items-start mb-2">
                                                <span className="text-slate-500"># 1. Create a video job</span>
                                                <Copy className="h-4 w-4 text-slate-600 cursor-pointer hover:text-white" />
                                            </div>
                                            <pre className="text-blue-300">import <span className="text-white">requests</span></pre>
                                            <pre className="mt-2">
                                                {`response = requests.post(
  "https://api.vidsimplify.com/v1/videos",
  headers={"Authorization": "Bearer YOUR_API_KEY"},
  json={
    "prompt": "Explain database sharding",
    "category": "tech_system",
    "duration_minutes": 5
  }
)

job_id = response.json()["job_id"]
print(f"Job started: {job_id}")`}
                                            </pre>
                                        </div>
                                    </TabsContent>

                                    <TabsContent value="curl">
                                        <div className="bg-slate-950 p-4 rounded-lg border border-slate-800 font-mono text-sm text-slate-300 overflow-x-auto">
                                            <pre>
                                                {`curl -X POST https://api.vidsimplify.com/v1/videos \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "prompt": "Explain database sharding",
    "category": "tech_system"
  }'`}
                                            </pre>
                                        </div>
                                    </TabsContent>
                                </Tabs>
                            </CardContent>
                        </Card>

                        <Card className="bg-slate-900 border-slate-800">
                            <CardHeader>
                                <CardTitle className="text-white">Endpoints</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-4">
                                {[
                                    { method: "POST", path: "/v1/videos", desc: "Create a new video generation job" },
                                    { method: "GET", path: "/v1/jobs/{job_id}", desc: "Check generation status and progress" },
                                    { method: "GET", path: "/v1/videos/{video_id}/download", desc: "Get secure download URL" },
                                    { method: "GET", path: "/v1/usage", desc: "Get current billing period usage" }
                                ].map((ep, i) => (
                                    <div key={i} className="flex items-center justify-between p-3 rounded bg-slate-950/50 border border-slate-800/50">
                                        <div className="flex items-center gap-3">
                                            <span className={`px-2 py-1 rounded text-xs font-bold ${ep.method === "POST" ? "bg-blue-900/30 text-blue-400" : "bg-green-900/30 text-green-400"
                                                }`}>
                                                {ep.method}
                                            </span>
                                            <span className="font-mono text-sm text-slate-300">{ep.path}</span>
                                        </div>
                                        <span className="text-sm text-slate-500">{ep.desc}</span>
                                    </div>
                                ))}
                            </CardContent>
                        </Card>
                    </div>

                    {/* Sidebar / Dashboard Simulation */}
                    <div className="space-y-6">
                        <Card className="bg-slate-900 border-slate-800">
                            <CardHeader>
                                <CardTitle className="text-white flex items-center gap-2">
                                    <BarChart3 className="h-5 w-5 text-green-400" />
                                    Usage & Cost
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="space-y-6">
                                    <div>
                                        <div className="flex justify-between text-sm mb-2">
                                            <span className="text-slate-400">API Calls</span>
                                            <span className="text-white font-medium">8,432 / 10,000</span>
                                        </div>
                                        <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                                            <div className="h-full w-[84%] bg-blue-500"></div>
                                        </div>
                                    </div>

                                    <div>
                                        <div className="flex justify-between text-sm mb-2">
                                            <span className="text-slate-400">Video Minutes</span>
                                            <span className="text-white font-medium">450 / 500</span>
                                        </div>
                                        <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                                            <div className="h-full w-[90%] bg-purple-500"></div>
                                        </div>
                                    </div>

                                    <div className="pt-4 border-t border-slate-800">
                                        <div className="flex justify-between items-center">
                                            <span className="text-slate-400">Current Bill</span>
                                            <span className="text-2xl font-bold text-white">$45.00</span>
                                        </div>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>

                        <div className="bg-gradient-to-br from-blue-900/20 to-violet-900/20 border border-blue-500/20 rounded-xl p-6">
                            <h3 className="text-lg font-semibold text-white mb-2">Enterprise Plan</h3>
                            <p className="text-sm text-slate-400 mb-4">
                                Need higher limits or dedicated rendering clusters?
                            </p>
                            <Button className="w-full bg-white text-slate-900 hover:bg-slate-200">
                                Contact Sales
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
