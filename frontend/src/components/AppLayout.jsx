import {useState} from "react";
import {Box, Flex} from "@chakra-ui/react";
import {Sidebar} from "./Sidebar/Sidebar";
import {NavBar} from "./Navbar/Navbar";

export const AppLayout = ({children}) => {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleCollapse = () => {
        setIsCollapsed(!isCollapsed);
    };

    const sidebarWidth = isCollapsed ? 'iconWidth' : '200px'; // Adjust depending on the width of your icons

    return (
        <Flex direction="row" h="100vh">
            {/* Sidebar */}
            <Box width={sidebarWidth}>
                <Sidebar isCollapsed={isCollapsed} onToggleCollapse={toggleCollapse}/>
            </Box>

            {/* Main Content */}
            <Box flexGrow={1}>
                <Box p='4'>
                    <NavBar/>
                    {children}
                </Box>
            </Box>
        </Flex>
    )
}