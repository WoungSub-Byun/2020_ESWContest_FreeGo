package com.example.myapplication;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.myapplication.retrofit.DTO.Food;
import com.example.myapplication.retrofit.DTO.FoodData;

import java.util.ArrayList;

public class ItemListAdapter extends BaseAdapter {

    Context context;
    ArrayList<Food> food;
    int resource;

    ItemListAdapter(Context context, ArrayList<Food> food, int resource){
        this.context = context;
        this.food = food;
        this.resource = resource;
    }


    @Override
    public int getCount() {
        return food.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if(convertView == null){
            LayoutInflater inflater = LayoutInflater.from(context);
            convertView = inflater.inflate(resource, parent);
        }
        ImageView foodImage = convertView.findViewById(R.id.foodImage);
        TextView foodTitle = convertView.findViewById(R.id.foodTitle);
        TextView foodDate = convertView.findViewById(R.id.foodDate);
        Button btnDelete = convertView.findViewById(R.id.btnDelete);
        btnDelete.setOnClickListener(v -> {
            DeleteDialog dialog = new DeleteDialog(context, new DialogClickListener() {
                @Override
                public void onAccept() {
                    //삭제 다이얼로그에서 예를 눌렀을때의 코드
                }

                @Override
                public void onCancel() {}
            });
            dialog.setCancelable(true);
            dialog.setCanceledOnTouchOutside(true);
            dialog.show();
        });


        return convertView;
    }
}
