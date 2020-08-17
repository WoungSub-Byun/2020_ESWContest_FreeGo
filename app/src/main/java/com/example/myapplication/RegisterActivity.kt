package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_register.*

class RegisterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)
        btnNext.setOnClickListener {
            if(nameText.text.toString().isNotEmpty()){
                val intent = Intent(this@RegisterActivity, WelcomeActivity::class.java)
                intent.putExtra("name",nameText.text.toString())
                startActivity(intent)
                finish()
            }
        }
    }
}