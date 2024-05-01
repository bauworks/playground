<?php

if (!defined('ABSPATH')) exit;

// Authentication
add_action('after_setup_theme', function() {

    $in_cli = (defined('WP_CLI') && WP_CLI);

    if($in_cli === false) {

        global $hcms;
        $auth_required = (boolean) $hcms->getSettingValue('auth_required');

        if($auth_required === true && !is_user_logged_in()) {

            $message = 'ログインしてください。';

            wp_die($message, $message, [
                'response' => 401
            ]);

        }

    }

});

add_action('template_redirect', function() {

    global $hcms;

    $url = $hcms->getRestApiUrl();
    wp_redirect($url);
    die();

});

add_action('admin_menu', function() {

    $page_name = HEADLRESS_CMSIZE_PLUGIN_NAME;
    add_menu_page($page_name, $page_name, 'administrator', 'headless-cmsize-top', function() {

        global $wpdb, $hcms;

        if($_SERVER['REQUEST_METHOD'] === 'POST') {

            $auth_required = isset($_POST['auth_required']) ? 1 : 0;
            $sql = 'SELECT COUNT(*) '.
                'FROM '. HEADLRESS_CMSIZE_TABLE_NAME. ' '.
                'WHERE name = "auth_required"';
            $auth_required_exists = (boolean) $wpdb->get_var($sql);

            if($auth_required_exists === true) {

                $sql = 'UPDATE '. HEADLRESS_CMSIZE_TABLE_NAME. ' '.
                    'SET value = %d '.
                    'WHERE name = "auth_required"';
                $wpdb->query(
                    $wpdb->prepare($sql, $auth_required)
                );

            } else {

                $sql = 'INSERT INTO '. HEADLRESS_CMSIZE_TABLE_NAME. ' '.
                    '(name, value) '.
                    'VALUES '.
                    '("auth_required", %d) ';
                $wpdb->query(
                    $wpdb->prepare($sql, $auth_required)
                );

            }

        }

        // Settings
        $results = $wpdb->get_results('SELECT * FROM '. HEADLRESS_CMSIZE_TABLE_NAME, ARRAY_A);
        $settings = [];

        foreach($results as $result) {

            $setting_name = $result['name'];
            $setting_value = $result['value'];
            $settings[$setting_name] = $setting_value;

        }

        $categories = $hcms->getCategories();

        require_once __DIR__ .'/../views/settings.php';

    });

});