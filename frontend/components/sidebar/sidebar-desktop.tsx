"use client";

import {SidebarButton} from "@/components/sidebar/sidebar-button";
import {BarChart, Check, Home} from "lucide-react";
import {SidebarItems} from "@/types";
import Link from "next/link";
import {Card, CardContent, CardFooter, CardHeader, CardTitle} from "@/components/ui/card";
import {Avatar, AvatarFallback, AvatarImage} from "@/components/ui/avatar";
import {Badge} from "@/components/ui/badge";

interface SidebarProps {
    sidebarItems: SidebarItems;
}

export function SidebarDesktop(props: SidebarProps) {
    return (
        <aside className="w-[270px] max-w-xs h-screen fixed left-0 top-0 z-40 border-r">
            <div className="h-full px-3 py-4 flex flex-col">
                {/*TODO: Make the card smaller and remove the link*/}
                <Card
                    className="bg-white shadow-md rounded-lg overflow-hidden transition-all ease-in-out duration-300 hover:shadow-xl">
                    <a href="#" rel="noopener noreferrer" target="_blank">
                        <CardContent className="flex flex-row items-center gap-4 p-6">
                            <Avatar>
                                <AvatarImage
                                    alt="Channel Logo"
                                    className="rounded-full object-cover aspect-square"
                                    src="/placeholder.svg?height=40&width=40"
                                />
                                <AvatarFallback>YT</AvatarFallback>
                            </Avatar>
                            <div className="space-y-1">
                                <h2 className="text-lg font-semibold">Yousef Baitalmal</h2>
                                <Badge className="text-xs" variant="secondary">
                                    ybaitalmal@panda.com.sa
                                </Badge>
                            </div>
                        </CardContent>
                    </a>
                </Card>

                <div className="flex flex-col gap-1 w-full">
                    {props.sidebarItems.links.map((link, index) => (
                        <Link key={index} href={link.href}>
                            <SidebarButton
                                className="w-full"
                                icon={link.icon}
                            >{link.label}</SidebarButton>
                        </Link>
                    ))}
                    {props.sidebarItems.extras}
                </div>
            </div>
        </aside>
    )
}