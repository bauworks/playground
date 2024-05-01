<?php
/*
Plugin Name: ヘッドレス CMSize
Description: WordPressをヘッドレスCMS化するプラグイン
Version: 1.0
Author: Sukohi Kuhoh
License: GPLv2 (or later)
*/

if (!defined('ABSPATH')) exit;

require_once __DIR__ .'/classes/Headless_Cmsize.php';
$hcms = new Headless_Cmsize();

require_once(__DIR__. '/includes/constants.php');
require_once(__DIR__. '/includes/activation.php');
require_once(__DIR__. '/includes/action.php');