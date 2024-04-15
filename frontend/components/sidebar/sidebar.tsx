"use client";

import {SidebarDesktop} from "@/components/sidebar/sidebar-desktop";
import {BarChart, Check, Home} from "lucide-react";
import {SidebarItems} from "@/types";
import {SidebarButton} from "@/components/sidebar/sidebar-button";

const sidebarItems: SidebarItems = {
    links: [
        {label: "Dashboard", href: "/", icon: Home},
        {label: "My Tasks", href: "/tasks", icon: Check},
        {label: "Analytics", href: "/analytics", icon: BarChart}
    ],
    extras: (
        <SidebarButton className="w-full justify-center gap-2 text-white" variant="default">Create Task</SidebarButton>
    )
}

export function Sidebar() {
    return (
        <SidebarDesktop sidebarItems={sidebarItems}/>
    )
}