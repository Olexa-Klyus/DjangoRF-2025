import {apiServiceAllowAny} from "./apiService";
import {urls} from "../constants/urls";

const categoryService = {
    getAll:async () =>{
        const response = await apiServiceAllowAny.get(urls.categories)
        return response.data;
    }
}
export {
    categoryService
}