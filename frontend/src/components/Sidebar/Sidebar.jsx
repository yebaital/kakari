import {Box, Button, Flex, List, Text} from "@chakra-ui/react";
import {FaBars, FaTasks, FaUser} from "react-icons/fa";
import {Icon} from "@chakra-ui/icons";

export const Sidebar = ({isCollapsed, onToggleCollapse}) => {

    const menuItems = [
        {id: 1, name: 'Dashboard', icon: FaUser},
        {id: 2, name: 'Item 2', icon: FaTasks},
    ];

    if (isCollapsed) {
        // Sidebar collapsed: render only icons
        return (
            <Flex direction="column" alignItems="center">
                <Button onClick={onToggleCollapse}>
                    <FaBars/>
                </Button>
                {menuItems.map(item => (
                    <Icon minW='60px' as={item.icon}/>
                ))}
            </Flex>
        );
    }

    // Sidebar not collapsed: render full content
    return (
        <Box>
            <Button onClick={onToggleCollapse}>
                <FaBars/>
            </Button>
            <List spacing={3}>
                {menuItems.map(item => (
                    <Flex alignItems="center">
                        <Box as={item.icon} fontSize="20px" mr={2} />
                        <Text>{item.name}</Text>
                    </Flex>
                ))}
            </List>
        </Box>
    );
};