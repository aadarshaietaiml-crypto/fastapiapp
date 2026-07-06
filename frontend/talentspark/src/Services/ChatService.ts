import api from "./api";
import type { ChatResponse } from "../types/chat";

export async function askChat(message: string, session_id: string): Promise<string> {
    const response = await api.post<ChatResponse>("/chat/", {
        message,
        session_id,
    });

    return response.data.reply;
}

export async function askCareerChat(message: string, session_id: string): Promise<string> {
    const response = await api.post<ChatResponse>("/chat/", {
        message,
        session_id,
    });

    return response.data.reply;
}