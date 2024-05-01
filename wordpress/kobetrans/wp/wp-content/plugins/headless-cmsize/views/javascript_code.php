<?php

$code = <<< END
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div id="app" class="p-5 w-50">
    <div v-if="isStatusIndex">
        <div v-if="announcements.length">
            <ul v-for="announcement in announcements">
                <li>
                    <a href="#" v-text="announcement.title.rendered" @click.prevent="showDetail(announcement.id)"></a>
                </li>
            </ul>
            <nav aria-label="Page navigation">
                <ul class="pagination">
                    <li class="page-item" :class="{ disabled: !hasPrevPage }" @click.prevent="movePage('prev')"><a class="page-link" href="#">前へ</a></li>
                    <li class="page-item" :class="{ disabled: !hasNextPage }" @click.prevent="movePage('next')"><a class="page-link" href="#">次へ</a></li>
                </ul>
            </nav>
        </div>
        <div v-else>まだお知らせはありません。</div>
    </div>
    <div v-if="isStatusShow">
        <div class="card mb-3">
            <div class="card-header" v-text="currentAnnouncement.title.rendered"></div>
            <div class="card-body" v-html="currentAnnouncement.content.rendered"></div>
        </div>
        <button class="btn btn-secondary" @click="setStatus('index')">戻る</button>
    </div>
</div>
<script src="https://unpkg.com/vue@3.2.31/dist/vue.global.prod.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.26.1/axios.min.js"></script>
<script>

    const { createApp, ref, computed, onMounted } = Vue;

    createApp({
        setup() {

            // 表示ステータス
            let status = ref('index');
            const isStatusIndex = computed(() => status.value === 'index');
            const isStatusShow = computed(() => status.value === 'show');
            const setStatus = newStatus => {

                status.value = newStatus;

            };

            // お知らせ一覧
            let announcements = ref([]);
            let pagination = ref({});
            let page = ref(1);
            const perPage = __PER_PAGE__;
            const getPosts = () => {

                const url = '{$hcms->getRestApiPostUrl()}';
                const params = {
                    params: {
                        page: page.value,
                        per_page: perPage,
                        orderby: 'date',
                        order: 'desc',
                        __CATEGORY_IDS__
                    }
                }

                axios.get(url, params)
                    .then(response => {

                        announcements.value = response.data;
                        pagination.value = {
                            total_pages: response.headers['x-wp-totalpages'],
                        };

                    });

            };
            const movePage = direction => {

                if (direction === 'prev' && hasPrevPage.value) {

                    page.value--;

                } else if (direction === 'next' && hasNextPage.value) {

                    page.value++;

                }

                getPosts();

            };
            const hasPrevPage = computed(() => {

                return page.value > 1;

            });
            const hasNextPage = computed(() => {

                return pagination.value.total_pages > page.value;

            });
            onMounted(() => {

                getPosts();

            });

            // お知らせ詳細
            let currentAnnouncementId = ref(-1);
            const currentAnnouncement = computed(() => {

                return announcements.value.find(announcement => {

                    return Number(announcement.id) === Number(currentAnnouncementId.value)

                });

            });
            const showDetail = (announcementId) => {

                currentAnnouncementId.value = announcementId;
                status.value = 'show';

            };

            return {
                isStatusIndex,
                isStatusShow,
                setStatus,
                announcements,
                movePage,
                hasPrevPage,
                hasNextPage,
                currentAnnouncement,
                showDetail
            }

        }
    })
    .mount('#app');

</script>
</body>
</html>
END;

echo htmlspecialchars($code, ENT_QUOTES, 'UTF-8');