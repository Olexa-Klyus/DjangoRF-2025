import {apiServiceAllowAny} from "./apiService";
import {urls} from "../constants/urls";

const categoryService = {
    getAll: async () => {
        const response = await apiServiceAllowAny.get(urls.categories)
        return response.data;
    }
}
const markService = {
    getById: async (id) => {
        const response = await apiServiceAllowAny.get(urls.brands(+id))
        return response.data;
    }
}


export {
    categoryService, markService
}