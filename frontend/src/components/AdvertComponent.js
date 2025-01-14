const AdvertComponent = ({advert}) => {
    return (
        <div>
            <div>{advert.description} - {advert.year}</div>
        </div>
    );
};

export {AdvertComponent};