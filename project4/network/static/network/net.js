document.addEventListener('DOMContentLoaded', function() {
            // Creating a post
            document.querySelector('form').onsubmit = function() {
                fetch("/post")
                    .then((response) => response.json())
                    .then((data) => {
                            for (let i = 0; i < data.posts.length; i++) {
                                // Loop threw the posts
                                const post = document.querySelector('#post').value;
                                const li = document.createElement('li')
                                document.querySelector('#posts').append(li);
                                li.innerHTML = `${data.posts[i]}, ${data.posts[i]}`;
                                document.getElementById('post').value = '';
                            }
                        })
                   return false;
                    };
            });


            If you want to add a new post, you’ll need to send the post data to the server, not just fetch existing posts.
            You can do this by modifying the fetch request to send a POST request with the new post data.
