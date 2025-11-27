const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type InputType = "text" | "url" | "pdf";
export type Category = "tech_system" | "product_startup" | "mathematical";
export type Quality = "low" | "medium" | "high" | "ultra";

export interface JobStatus {
    job_id: string;
    status: "pending" | "generating_code" | "rendering" | "completed" | "failed";
    progress: {
        percentage: number;
        message: string;
    };
    error?: string;
    output_url?: string;
    created_at: string;
}

export const api = {
    async createVideo(
        input_data: string,
        input_type: InputType,
        category: Category,
        quality: Quality = "high"
    ) {
        const response = await fetch(`${API_BASE_URL}/api/videos`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                input_data,
                input_type,
                category,
                quality,
            }),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Failed to create video job");
        }

        return response.json();
    },

    async getJobStatus(jobId: string): Promise<JobStatus> {
        const response = await fetch(`${API_BASE_URL}/api/jobs/${jobId}`);

        if (!response.ok) {
            throw new Error("Failed to get job status");
        }

        return response.json();
    },

    getVideoUrl(jobId: string) {
        return `${API_BASE_URL}/api/videos/${jobId}`;
    }
};
