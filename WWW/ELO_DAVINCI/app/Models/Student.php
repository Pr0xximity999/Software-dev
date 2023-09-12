<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Student extends Model
{
    use HasFactory;

    protected $table = 'students';

    protected $primaryKey = 'id';

    protected $fillable = [
        'studentnumber',
        'location',
        'school',
        'class',
        'firstname',
        'infix',
        'lastname',
        'initials',
        'street',
        'housenumber',
        'housenumber_suffix',
        'postal_code',
        'city',
        'Country_id',
    ];
}
