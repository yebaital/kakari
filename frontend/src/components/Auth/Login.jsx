import {Box, Center, Flex, FormControl, FormErrorMessage, Image, Link, Text, useToast, VStack} from "@chakra-ui/react";
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";
import StyledInput from "./StyledInput";
import StyledButton from "./StyledButton";
import {login} from "../../actions/authActions";
import {useDispatch, useSelector} from "react-redux";

export const Login = () => {
    const {
        handleSubmit,
        register,
        formState: {errors},
    } = useForm();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onSubmit = (values) => {
        dispatch(login(values.email, values.password));
    };

    const {isAuthenticated, user, loading, error} = useSelector(
        (state) => state.auth
    );

    const toast = useToast();

    // Check for error
    if (error) {
        toast({
            title: "Invalid email or password",
            status: "error",
            isClosable: true,
            duration: 1500,
        });
    }

    return <Flex width="full" height="100vh">

        {/* Left side */}
        <Box flex="1" backgroundColor="#017BD6">
            <Center height="100%">
                <Image src={`${process.env.PUBLIC_URL}/login.webp`} alt="Login Image" objectFit="cover" width="400px"/>
            </Center>
        </Box>

        {/* Right side */}
        <Box flex="1" padding="12" backgroundColor="#161616">
            <Center height="100%" width="full">
                <VStack spacing="8" width="full">
                    <Box width="50%" textAlign="center">
                        <Box marginBottom="1rem">
                            <Text textAlign="center" fontWeight="bold" fontSize="2xl" color="#ffffff">
                                Login
                            </Text>
                        </Box>
                        <form onSubmit={handleSubmit(onSubmit)}>
                            <FormControl isInvalid={errors.email}>
                                <StyledInput
                                    placeholder="Email"
                                    type="email"
                                    size="lg"
                                    marginTop="6"
                                    register={register("email", {
                                        required: "This is a required field",
                                    })}
                                />
                                <FormErrorMessage>
                                    {errors.email && <span>{errors.email.message}</span>}
                                </FormErrorMessage>
                            </FormControl>
                            <FormControl isInvalid={errors.password}>
                                <StyledInput
                                    placeholder="Password"
                                    type="password"
                                    size="lg"
                                    marginTop="6"
                                    register={register("password", {
                                        required: "This is a required field",
                                    })}
                                />
                                <FormErrorMessage>
                                    {errors.password && <span>{errors.password.message}</span>}
                                </FormErrorMessage>
                            </FormControl>
                            <StyledButton type="submit" mt={6}>
                                Login
                            </StyledButton>
                            <Box display="flex" justifyContent="center" alignItems="center" mt={4}>
                                <Link onClick={() => navigate("/register", {replace: true})}>
                                    <Text color="blue.500">
                                        Register Instead
                                    </Text>
                                </Link>
                            </Box>
                        </form>
                    </Box>
                </VStack>
            </Center>
        </Box>
    </Flex>
}