import Link from "next/link";
import { Video, Github, Twitter, Linkedin } from "lucide-react";

export function Footer() {
    return (
        <footer className="bg-slate-950 border-t border-white/5 pt-16 pb-8">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
                    <div className="col-span-1 md:col-span-1">
                        <Link href="/" className="flex items-center gap-2 mb-6">
                            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-violet-600">
                                <Video className="h-4 w-4 text-white" />
                            </div>
                            <span className="text-lg font-bold text-white">VidSimplify</span>
                        </Link>
                        <p className="text-slate-400 text-sm leading-relaxed mb-6">
                            Precision animation engine for the modern web. Explain complex systems with mathematical accuracy.
                        </p>
                        <div className="flex gap-4">
                            <Link href="#" className="text-slate-400 hover:text-white transition-colors">
                                <Twitter className="h-5 w-5" />
                            </Link>
                            <Link href="#" className="text-slate-400 hover:text-white transition-colors">
                                <Github className="h-5 w-5" />
                            </Link>
                            <Link href="#" className="text-slate-400 hover:text-white transition-colors">
                                <Linkedin className="h-5 w-5" />
                            </Link>
                        </div>
                    </div>

                    <div>
                        <h3 className="text-white font-semibold mb-4">Product</h3>
                        <ul className="space-y-3 text-sm text-slate-400">
                            <li><Link href="#features" className="hover:text-blue-400 transition-colors">Features</Link></li>
                            <li><Link href="#showcase" className="hover:text-blue-400 transition-colors">Showcase</Link></li>
                            <li><Link href="/api-docs" className="hover:text-blue-400 transition-colors">API</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Pricing</Link></li>
                        </ul>
                    </div>

                    <div>
                        <h3 className="text-white font-semibold mb-4">Resources</h3>
                        <ul className="space-y-3 text-sm text-slate-400">
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Documentation</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Blog</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Community</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Help Center</Link></li>
                        </ul>
                    </div>

                    <div>
                        <h3 className="text-white font-semibold mb-4">Legal</h3>
                        <ul className="space-y-3 text-sm text-slate-400">
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Privacy Policy</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Terms of Service</Link></li>
                            <li><Link href="#" className="hover:text-blue-400 transition-colors">Cookie Policy</Link></li>
                        </ul>
                    </div>
                </div>

                <div className="border-t border-white/5 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                    <p className="text-slate-500 text-sm">
                        © {new Date().getFullYear()} VidSimplify Inc. All rights reserved.
                    </p>
                    <div className="flex items-center gap-2 text-sm text-slate-500">
                        <div className="h-2 w-2 rounded-full bg-green-500"></div>
                        All Systems Operational
                    </div>
                </div>
            </div>
        </footer>
    );
}
