package com.example.myapplication.retrofit.API

import com.example.myapplication.retrofit.DTO.BarCodeFoodInfo
import com.example.myapplication.retrofit.DTO.FirstData
import com.example.myapplication.retrofit.DTO.FoodData
import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.GET
import retrofit2.http.POST

interface FridgeAPI {
    @GET("/init")
    fun getTable() : Call<FirstData>

    @POST("/show")
    fun showFood(
        @Field("id") id : String
    ) : Call<FoodData>

    @POST("/find")
    fun findFood(
        @Field("id") id : String,
        @Field("p_name") p_name : String
    ) : Call<FirstData>

    @POST("late")
    fun findLateFood(
        @Field("id") id : String
    ) : Call<FoodData>

    @POST("/insert")
    fun insertFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String,
        @Field("p_number") p_number : Int,
        @Field("p_ex_date") p_ex_date : String
    ) : Call<FirstData>

    @POST("/update")
    fun updateFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String,
        @Field("p_number") p_number: Int
    ) : Call<FirstData>

    @POST("/delete")
    fun deleteFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String
    ) : Call<FirstData>

    @POST("/lookupcode")
    fun barCodeShow(
        @Field("gtin") gtin : String
    ) : Call<BarCodeFoodInfo>

}