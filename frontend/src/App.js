import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App() {
    return <Router>
        <Routes>
            <Route path="/login" element={<h1>Login</h1>} />
            <Route path="/register" element={<h1>Register</h1>} />
        </Routes>
    </Router>;
}

export default App;
