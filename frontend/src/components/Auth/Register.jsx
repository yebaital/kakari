import {Box, Center, Flex, FormControl, FormErrorMessage, Image, VStack, Text, Link} from "@chakra-ui/react";
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";
import StyledInput from "./StyledInput";
import StyledButton from "./StyledButton";

export const Register = () => {
    const {
        handleSubmit,
        register,
        getValues,
        formState: {
            errors,
            isSubmitting
        }
    } = useForm();

    const onSubmit = (values) => {
        console.log(values)
    }

    const navigate = useNavigate()

    return <Flex width="full" height="100vh">

        {/* Left side */}
        <Box flex="1" backgroundColor="#017BD6">
            <Center height="100%">
                <Image src={`${process.env.PUBLIC_URL}/register.webp`} alt="Register Image" objectFit="cover"
                       width="400px"/>
            </Center>
        </Box>

        {/* Right side */}
        <Box flex="1" padding="12" backgroundColor="#161616">
            <Center height="100%" width="full">
                <VStack spacing="8" width="full">
                    <Box width="50%" textAlign="center">
                        <Box marginBottom="1rem">
                            <Text textAlign="center" fontWeight="bold" fontSize="2xl" color="#ffffff">
                                Register
                            </Text>
                        </Box>
                        <form onSubmit={handleSubmit(onSubmit)}>
                            <FormControl isInvalid={errors.email}>
                                <StyledInput
                                    placeholder="Full name"
                                    type="text"
                                    size="lg"
                                    marginTop="6"
                                    register={register("fullname", {
                                        required: "This is a required field",
                                    })}
                                />
                                <FormErrorMessage>
                                    {errors.fullname && <span>{errors.fullname.message}</span>}
                                </FormErrorMessage>
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
                                    register={
                                        register("password", {
                                            required: "This is a required field",
                                            minLength: {
                                                value: 6,
                                                message: "Password should be at least 6 characters long"
                                            },
                                            maxLength: {
                                                value: 24,
                                                message: "Password should be at most 24 characters long"
                                            }
                                        })
                                    }
                                />
                                <StyledInput
                                    placeholder="Verify Password"
                                    type="password"
                                    size="lg"
                                    marginTop="6"
                                    register={
                                        register("verifyPassword", {
                                            required: "This is a required field",
                                            validate: {
                                                matchesPreviousPassword: (value) => {
                                                    const {password} = getValues();
                                                    return password === value || "Passwords should match!";
                                                }
                                            }
                                        })
                                    }
                                />
                                <FormErrorMessage>
                                    {errors.password && <span>{errors.password.message}</span>}
                                </FormErrorMessage>
                                <FormErrorMessage>
                                    {errors.verifyPassword && <span>{errors.verifyPassword.message}</span>}
                                </FormErrorMessage>
                            </FormControl>
                            <StyledButton type="submit" mt={6} onClick={() => alert('Button Clicked')}>
                                Register
                            </StyledButton>
                            <Box display="flex" justifyContent="center" alignItems="center" mt={4}>
                                <Link onClick={() => navigate("/login", {replace: true})}>
                                    <Text color="blue.500">
                                        Login Instead
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