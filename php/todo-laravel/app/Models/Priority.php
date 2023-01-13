<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Priority extends Model
{
    use HasFactory;

    // モデルに関連付けるテーブル
    protected $table = 'priorities';

    // プライマリキー
    protected $primaryKey = 'id';

    // 登録・更新可能カラムの指定
    protected $fillable = [
        'id',
        'priority',
        'explanation',
        'rank',
        'created_at',
        'updated_at'
    ];

    // 全件データ取得
    public function findAllPriority()
    {
        return Priority::all();
    }
}
