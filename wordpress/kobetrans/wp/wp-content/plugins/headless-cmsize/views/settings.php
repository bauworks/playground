<?php

if (!defined('ABSPATH')) exit;

?>

<div id="headless_cmsize_app">

    <div class="wrap">
        <h1><?php echo HEADLRESS_CMSIZE_PLUGIN_NAME; ?></h1>
    </div>
    <form action="?page=headless-cmsize-top" method="POST">

        <h2>設定</h2>
        <table class="form-table">
            <tbody>
            <tr>
                <th scope="row">
                    <label for="headless-cmsize-top-url">
                        ログイン必須
                    </label>
                </th>
                <td>
                    <input type="checkbox" name="auth_required" value="1" <?php checked(1, $settings['auth_required']); ?>>
                    Rest API はログインを必須にする
                    <p class="description">
                        必須にする場合は、<a href="./profile.php#application-passwords-section">Application Password</a> を使ってアクセスしてください。<br>
                        <div style="color:#cc2222;padding-top:15px;font-size:80%;">
                            <strong>注意</strong>
                            <br>
                            Application Password は、必ず PHP などのサーバーサイドで使用してください。<br>
                            クライアントサイド（JavaScript）に記述すると、パスワードが公開状態になります。
                        </div>
                    </p>
                </td>
            </tr>
            </tbody>
        </table>

        <br>
        <button type="submit" class="button button-primary">
            <?php echo HEADLRESS_CMSIZE_PLUGIN_NAME; ?> の設定を保存する
        </button>

    </form>

    <br>
    <hr>

    <h2>JavaScript コード生成</h2>
    出力したいカテゴリを選択してください。<small>（カテゴリを分けると複数サイト向けに運用ができます）</small>
    <div class="card" style="margin-bottom:15px;">
        <span v-for="c in categories" style="float:left;padding:5px 20px 5px 0;">
            <label style="white-space:nowrap;">
                <input type="checkbox" :value="c.id" v-model="categoryIds"> {{ c.name }}
            </label>
        </span>
        <div style="clear:both;"></div>
    </div>
    １ページごとに表示する件数
    <div class="card" style="margin-bottom:15px;">
        <input type="number" v-model="perPage" min="1" style="width:80px;"> 件
    </div>

    <strong>
        生成されたコード
    </strong>

    <pre id="displaying_code" style="background:#ddd;padding:15px;margin-right:15px;height:200px;overflow:auto;" v-html="convertedJsCode"></pre>

    <button type="button" class="button button-primary" style="margin-right:5px;" @click="downloadCode">
        ダウンロードする
    </button>
    <button type="button" class="button button-primary" @click="copyCode">
        コピーする
    </button>
    <span style="color:#31a65a;padding-left:10px;">{{ copyMessage }}</span>

    <div style="padding-top:25px;">
        プラグイン作者： <a href="https://twitter.com/SukohiKuhoh" target="_blank">九保すこひ</a>
    </div>

</div>

<script>

    const { createApp, ref, reactive, computed, onMounted } = Vue;

    createApp({
        setup() {

            // JavaScript code
            const categories = reactive(<?php echo json_encode($categories); ?>);
            let categoryIds = ref([]);
            let perPage = ref(10);
            const jsCode = `<?php

                require_once __DIR__ .'/javascript_code.php'

            ?>`;
            const convertedJsCode = computed(() => {

                let code = jsCode;
                const joinedCategories = categoryIds.value.sort().join(',');
                const replacers = [
                    {
                        target: /__CATEGORY_IDS__/g,
                        replacement: (categoryIds.value.length > 0)
                            ? `categories: '${joinedCategories}'`
                            : '',
                    },
                    {
                        target: /__PER_PAGE__/g,
                        replacement: perPage.value,
                    },
                ];

                replacers.forEach(replacer => {

                    code = code.replace(replacer.target, replacer.replacement);

                });

                return code;

            });

            // Copy
            const getDisplayingCode = () => {

                return document.querySelector('#displaying_code').innerText;

            };
            const copyCode = () => {

                let textarea = document.createElement('textarea');
                textarea.value = getDisplayingCode();
                textarea.style.top = '-100px';
                textarea.style.maxHeight = '100px';
                textarea.style.position = 'absolute';
                document.body.appendChild(textarea);

                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);

                copyMessage.value = '【コピーしました】';

                setTimeout(() => {

                    copyMessage.value = '';

                }, 3000);

            };
            let copyMessage = ref('')

            // Download
            const downloadCode = () => {

                const code = getDisplayingCode();
                let blob = new Blob([code], { type: 'text/plain' });
                let url = window.URL.createObjectURL(blob);
                let a = document.createElement('a');
                a.href = url;
                a.download = 'headless-cms.html';
                a.click();

            };

            return {
                categories,
                categoryIds,
                perPage,
                convertedJsCode,
                copyCode,
                copyMessage,
                downloadCode
            };

        }
    })
    .mount('#headless_cmsize_app');

</script>