<?php

if (!defined('ABSPATH')) exit;

class Headless_Cmsize
{
    public function __construct()
    {
        $this->setAssets();
    }

    public function getSettingValue($name)
    {
        global $wpdb;

        $sql = 'SELECT value FROM '. HEADLRESS_CMSIZE_TABLE_NAME .' WHERE name = "%s"';

        return $wpdb->get_var(
            $wpdb->prepare($sql, $name)
        );
    }

    public function getCategories()
    {
        $categories = [];
        $category_terms = get_terms('category', [
            'fields' => 'all',
            'hide_empty' => false,
        ]);

        foreach($category_terms as $category_term) {

            $categories[] = [
                'id' => $category_term->term_id,
                'name' => $category_term->name,
            ];

        }

        return $categories;
    }

    public function getRestApiUrl()
    {
        return get_rest_url(null, 'wp/v2/');
    }

    public function getRestApiPostUrl()
    {
        return $this->getRestApiUrl() .'posts/';
    }

    private function setAssets()
    {
        wp_enqueue_script('vue', 'https://cdnjs.cloudflare.com/ajax/libs/vue/3.2.31/vue.global.prod.min.js', [], '3.2.31');
    }
}