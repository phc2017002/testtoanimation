import { Navbar } from "@/components/landing/Navbar";
import { Hero } from "@/components/landing/Hero";
import { Showcase } from "@/components/landing/Showcase";
import { Footer } from "@/components/landing/Footer";
import { Check, Edit, Layers, Zap } from "lucide-react";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950">
      <Navbar />
      <Hero />
      <Showcase />

      {/* Problem vs Solution Section */}
      <section className="py-24 bg-slate-900">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-16 items-center">
            <div>
              <h2 className="text-3xl font-bold text-white mb-6">
                The Problem with <span className="text-red-400">Random AI Video</span>
              </h2>
              <ul className="space-y-4">
                {[
                  "Hallucinated facts and visuals",
                  "Inconsistent style and branding",
                  "Impossible to edit specific details",
                  "Black box generation process"
                ].map((item, i) => (
                  <li key={i} className="flex items-center text-slate-400">
                    <div className="h-2 w-2 rounded-full bg-red-500 mr-3" />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h2 className="text-3xl font-bold text-white mb-6">
                The <span className="text-blue-400">VidSimplify</span> Solution
              </h2>
              <ul className="space-y-4">
                {[
                  "Mathematically precise animations",
                  "Granular control over every detail",
                  "Consistent, professional styling",
                  "Explainable and transparent generation"
                ].map((item, i) => (
                  <li key={i} className="flex items-center text-slate-300">
                    <div className="h-6 w-6 rounded-full bg-blue-500/20 text-blue-400 flex items-center justify-center mr-3">
                      <Check className="h-4 w-4" />
                    </div>
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section id="features" className="py-24 bg-slate-950">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Engineered for Complexity
            </h2>
            <p className="mt-4 text-lg text-slate-400 max-w-2xl mx-auto">
              In a growing complex world, we need tools that can explain the working of any system, research, or product in depth.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                title: "Multi-Dimensional",
                description: "Generate 2D and 3D visualizations that capture every angle of your concept.",
                icon: <Layers className="h-8 w-8 text-blue-400" />
              },
              {
                title: "Fully Editable",
                description: "Don't like a color? Want to change a speed? Tweak parameters instantly.",
                icon: <Edit className="h-8 w-8 text-violet-400" />
              },
              {
                title: "Instant Repurposing",
                description: "Generate once, then tweak for different formats, audiences, and platforms.",
                icon: <Zap className="h-8 w-8 text-indigo-400" />
              }
            ].map((feature, i) => (
              <div key={i} className="bg-slate-900/50 border border-white/5 p-8 rounded-2xl hover:bg-slate-900 transition-colors">
                <div className="mb-6 bg-slate-800/50 w-16 h-16 rounded-xl flex items-center justify-center border border-white/5">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-white mb-3">{feature.title}</h3>
                <p className="text-slate-400 leading-relaxed">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}
