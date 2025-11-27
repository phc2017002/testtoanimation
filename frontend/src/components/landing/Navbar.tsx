"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Video, Menu, X } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";

export function Navbar() {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    return (
        <nav className="fixed top-0 w-full z-50 border-b border-white/5 bg-slate-950/80 backdrop-blur-md">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="flex h-16 items-center justify-between">
                    <div className="flex items-center gap-2">
                        <Link href="/" className="flex items-center gap-2">
                            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-violet-600">
                                <Video className="h-4 w-4 text-white" />
                            </div>
                            <span className="text-lg font-bold text-white">VidSimplify</span>
                        </Link>
                    </div>

                    {/* Desktop Menu */}
                    <div className="hidden md:block">
                        <div className="flex items-center gap-8">
                            <Link href="/#features" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">
                                Features
                            </Link>
                            <Link href="/#showcase" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">
                                Showcase
                            </Link>
                            <Link href="/api-docs" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">
                                API
                            </Link>
                            <Link href="/pricing" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">
                                Pricing
                            </Link>
                        </div>
                    </div>

                    <div className="hidden md:flex items-center gap-4">
                        <Link href="/login" className="text-sm font-medium text-slate-400 hover:text-white">
                            Log in
                        </Link>
                        <Link href="/app">
                            <Button className="bg-white text-slate-900 hover:bg-slate-200 font-medium">
                                Get Started
                            </Button>
                        </Link>
                    </div>

                    {/* Mobile Menu Button */}
                    <div className="md:hidden">
                        <button
                            onClick={() => setIsMenuOpen(!isMenuOpen)}
                            className="text-slate-400 hover:text-white p-2"
                        >
                            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu Dropdown */}
            <AnimatePresence>
                {isMenuOpen && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                        className="md:hidden border-t border-white/5 bg-slate-950"
                    >
                        <div className="space-y-1 px-4 pb-3 pt-2">
                            <Link
                                href="/#features"
                                className="block px-3 py-2 text-base font-medium text-slate-400 hover:bg-slate-900 hover:text-white rounded-md"
                                onClick={() => setIsMenuOpen(false)}
                            >
                                Features
                            </Link>
                            <Link
                                href="/#showcase"
                                className="block px-3 py-2 text-base font-medium text-slate-400 hover:bg-slate-900 hover:text-white rounded-md"
                                onClick={() => setIsMenuOpen(false)}
                            >
                                Showcase
                            </Link>
                            <Link
                                href="/api-docs"
                                className="block px-3 py-2 text-base font-medium text-slate-400 hover:bg-slate-900 hover:text-white rounded-md"
                                onClick={() => setIsMenuOpen(false)}
                            >
                                API
                            </Link>
                            <Link
                                href="/pricing"
                                className="block px-3 py-2 text-base font-medium text-slate-400 hover:bg-slate-900 hover:text-white rounded-md"
                                onClick={() => setIsMenuOpen(false)}
                            >
                                Pricing
                            </Link>
                            <div className="mt-4 pt-4 border-t border-white/5 flex flex-col gap-3">
                                <Link
                                    href="/login"
                                    className="block px-3 py-2 text-base font-medium text-slate-400 hover:bg-slate-900 hover:text-white rounded-md"
                                    onClick={() => setIsMenuOpen(false)}
                                >
                                    Log in
                                </Link>
                                <Link href="/app" onClick={() => setIsMenuOpen(false)}>
                                    <Button className="w-full bg-white text-slate-900 hover:bg-slate-200 font-medium">
                                        Get Started
                                    </Button>
                                </Link>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </nav>
    );
}
