<?php

if (!defined('ABSPATH')) exit;

// Activation
register_activation_hook( __FILE__, function() {

    global $wpdb;
    $test_db_version = '1.0.0';
    $charset_collate = $wpdb->get_charset_collate();
    $sql = 'CREATE TABLE IF NOT EXISTS `'. HEADLRESS_CMSIZE_TABLE_NAME .'` (
            id int(11) NOT NULL auto_increment primary key,
            name varchar(255) NOT NULL,
            value varchar(255) NOT NULL
    ) '. $charset_collate .';';

    require_once(ABSPATH .'wp-admin/includes/upgrade.php');
    dbDelta($sql);
    add_option( 'test_db_version', $test_db_version );

});