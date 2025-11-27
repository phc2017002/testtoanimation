import { Suspense } from "react";
import { VideoGenerator } from "@/components/app/VideoGenerator";

export const dynamic = "force-dynamic";

export default function AppPage() {
    return (
        <Suspense fallback={<div className="flex items-center justify-center h-screen bg-slate-950 text-slate-400">Loading...</div>}>
            <VideoGenerator />
        </Suspense>
    );
}
