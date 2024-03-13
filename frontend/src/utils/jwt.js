import jwt_decode from 'jwt-decode'

/**
 * Function to validate a token.
 *
 * @param {string} token - The token to be validated.
 *
 * @returns {boolean} - Returns true if the token is valid, otherwise returns false.
 */
export const validateToken = (token) => {
    const now = Math.round(new Date().getTime() / 1000)
    const decodedToken = jwt_decode(token)
    return decodedToken && now < decodedToken.exp
}