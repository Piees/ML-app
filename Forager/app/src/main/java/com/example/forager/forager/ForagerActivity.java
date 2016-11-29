package com.example.forager;

import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.example.forager.forager.R;

public class ForagerActivity extends Activity {

    Button btnTakePhoto;
    Button btnPickPhoto;
    Button btnGenPhoto;

    ImageView imgTakenPhoto;

    private static final int CAM_REQUEST = 1;
    public final static int PICK_PHOTO_CODE = 2;
    public final static int GEN_PHOTO_REQUEST = 3;

    private String selectedImagePath;
    private String filemanagerstring;

    private static final String url = "http://127.0.0.1:5000/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        btnTakePhoto = (Button) findViewById(R.id.t_photo);
        btnPickPhoto = (Button) findViewById(R.id.p_photo);
        btnGenPhoto = (Button) findViewById(R.id.g_photo);


        imgTakenPhoto = (ImageView) findViewById(R.id.imageview1);

        btnTakePhoto.setOnClickListener(new btnTakePhotoClicker());
        btnPickPhoto.setOnClickListener(new btnPickPhotoClicker());
        btnGenPhoto.setOnClickListener(new btnGenPhotoClicker());
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // TODO Auto-generated method stub
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == CAM_REQUEST) {
            resetimage();
            Bitmap thumbnail = (Bitmap) data.getExtras().get("data");
            imgTakenPhoto.setImageBitmap(thumbnail);
            Toast.makeText(getApplicationContext(), "Photo is taken", Toast.LENGTH_SHORT).show();
        }

        if(requestCode == PICK_PHOTO_CODE)
        {
            resetimage();
            Uri selectedImageUri = data.getData();
            imgTakenPhoto.setImageURI(selectedImageUri);
            Toast.makeText(getApplicationContext(), selectedImageUri.toString(), Toast.LENGTH_SHORT).show();

            //OI FILE Manager
            filemanagerstring = selectedImageUri.getPath();

            //MEDIA GALLERY
            selectedImagePath = getPath(selectedImageUri);
        }

    }

    public String getPath(Uri uri) {
        String[] projection = { MediaStore.Images.Media.DATA };
        Cursor cursor = managedQuery(uri, projection, null, null, null);
        if(cursor!=null)
        {
            int column_index = cursor
                    .getColumnIndexOrThrow(MediaStore.Images.Media.DATA);
            cursor.moveToFirst();
            return cursor.getString(column_index);
        }
        else return null;
    }


    class btnGenPhotoClicker implements Button.OnClickListener {
        public void onClick(View v) {
            Toast.makeText(getApplicationContext(), url, Toast.LENGTH_SHORT).show();

        }
    }

    class btnTakePhotoClicker implements Button.OnClickListener {
        // go to camera
        @Override
        public void onClick(View v) {
            // TODO Auto-generated method stub
            Intent cameraintent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
            startActivityForResult(cameraintent, CAM_REQUEST);
        }
    }


    class btnPickPhotoClicker implements Button.OnClickListener {
        // go to album
        @Override
        public void onClick(View v) {
            //TODO Auto-generated method stub
            Intent albumintent = new Intent();
            albumintent.setType("image/*");
            albumintent.setAction(Intent.ACTION_GET_CONTENT);
            startActivityForResult(Intent.createChooser(albumintent,"Select Picture" ),PICK_PHOTO_CODE);
        }
    }

    public void resetimage() {
        imgTakenPhoto.invalidate();
    }


}
