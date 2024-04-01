import {Box, Flex, VStack, Text, Image} from "@chakra-ui/react";

export const ProfileCard = ({imgSrc, name, email}) => {
    return (
        <Flex bg="white" boxShadow="md" px={1} py={2} mb={2} rounded="lg" align="center" w="200px" background="#161616" color="#ffffff">
            <Box flexShrink={0} w="35px">
                <Image
                    borderRadius="full"
                    boxSize="35px"
                    objectFit="cover"
                    src={imgSrc}
                    alt={name}
                />
            </Box>
            <VStack align="start" ml={4} isTruncated>
                <Text style={{fontSize: 'clamp(0.6rem, 4vw, 0.9rem)'}} fontWeight="bold">{name}</Text>
                <Text style={{fontSize: 'clamp(0.4rem, 3vw, 0.7rem)'}} >{email}</Text>
            </VStack>
        </Flex>
    )
}