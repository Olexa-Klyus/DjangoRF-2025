import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";

import {AdvertsPage} from "./pages/AdvertsPage";
import {ChatPage} from "./pages/ChatPage";
import {LoginPage} from "./pages/LoginPage";
import {RegisterPage} from "./pages/RegisterPage";
import {ActivatePage} from "./pages/ActivatePage";
import {AdvertInfoPage} from "./pages/AdvertInfoPage";
import {AdvertFormComponent} from "./components/AdvertFormComponent/AdvertFormComponent";
import NewPage from "./pages/NewPage";

const router = createBrowserRouter([
    {
        path: '/', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'login'}/>},
            {path: 'login', element: <LoginPage/>},
            {path: 'register', element: <RegisterPage/>},

            {path: 'adverts', element: <AdvertsPage/>},
            {path: 'adverts/advert_info/:id', element: <AdvertInfoPage/>},
            {path: 'adverts/add', element: <AdvertFormComponent/>},
            {path: 'adverts/update/:id', element: <AdvertFormComponent/>},


            {path: 'select', element: <NewPage/>},
            {path: 'chat', element: <ChatPage/>},
            {path: 'activate/:token', element: <ActivatePage/>},

        ]
    }
])

export {
    router
}