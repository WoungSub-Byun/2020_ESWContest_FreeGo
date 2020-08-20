package com.example.myapplication

import android.annotation.SuppressLint
import android.content.Context
import android.graphics.Color
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import com.google.android.material.bottomnavigation.BottomNavigationView
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import com.example.myapplication.retrofit.API.RetrofitHelper
import com.example.myapplication.retrofit.DTO.Food
import com.example.myapplication.retrofit.DTO.FoodData
import kotlinx.android.synthetic.main.activity_fridge.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class FridgeActivity : AppCompatActivity() {


    @SuppressLint("ResourceType")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fridge)

        val id: String? = getData()
        var dataList = ArrayList<Food>()

        if(id != null){
            val service = RetrofitHelper().getRetrofit()

            service.showFood(id).enqueue(object : Callback<FoodData>{
                override fun onFailure(call: Call<FoodData>, t: Throwable) {
                    Log.d("ERROR",t.toString())
                }

                override fun onResponse(call: Call<FoodData>, response: Response<FoodData>) {
                    if(response.isSuccessful) {
                        Log.d("CODE", response.body()!!.code.toString())
                        if (response.body()!!.code == 200) {
                            dataList = response.body()!!.data
                            Log.d("MESSAGE", response.body()!!.message)
                            val adapter =
                                ItemListAdapter(this@FridgeActivity, dataList, R.layout.food_row)
                            itemList.adapter = adapter
                        }
                    }
                }
            })

            itemList.setOnItemClickListener{ parent: AdapterView<*>, view: View, position: Int, id: Long ->
                //intent로 dataList position 번째 데이터를 모두 옮긴다.
            }
        }
        else {
            textView3.alpha = 1f
            itemList.setBackgroundResource(Color.GRAY)
        }

    }

    fun saveData(id : String){
        val pref = getSharedPreferences("id", Context.MODE_PRIVATE)
        val editor = pref.edit()
        editor.putString("id",id)
        editor.apply()
    }

    fun getData() : String? {
        val pref = getSharedPreferences("id", Context.MODE_PRIVATE)
        return pref.getString("id",null)
    }
}