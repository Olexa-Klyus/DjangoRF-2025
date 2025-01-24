import React from 'react';
import {Link} from "react-router-dom";

const HeaderComponent = () => {
    return (
        <div>
            <header>
                <Link to="/register"> RegisterPage </Link>
                <Link to="/login"> LoginPage </Link>
                <Link to="/adverts"> AdvertsPage </Link>
                <Link to="/chat"> ChatPage </Link>
                <Link to="/adverts/advert_info/2"> AdvertInfoPage </Link>
            </header>
            <br/>
        </div>
    );
};

export default HeaderComponent;