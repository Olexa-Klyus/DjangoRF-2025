import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";

import {AdvertsPage} from "./pages/AdvertsPage";
import {ChatPage} from "./pages/ChatPage";
import {LoginPage} from "./pages/LoginPage";
import {RegisterPage} from "./pages/RegisterPage";
import {ActivatePage} from "./pages/ActivatePage";

const router = createBrowserRouter([
    {
        path: '/', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'login'}/>},
            {path: 'login', element: <LoginPage/>},
            {path: 'register', element: <RegisterPage/>},
            {path: 'adverts', element: <AdvertsPage/>},
            {path: 'chat', element: <ChatPage/>},
            {path: 'activate/:token', element: <ActivatePage/>}

        ]
    }
])

export {
    router
}