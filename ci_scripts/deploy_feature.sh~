#!/bin/bash
cdir=$(basename "$PWD")
echo $cdir
ssh root@188.166.187.156 'bash -s' < script.sh /home/dev/temp/feature/$cdir
rm -rfv ./.git
rm -rfv ./venv
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/feature/$cdir
ssh root@188.166.187.156 'bash -s' < script1.sh /home/dev/temp/feature


source /opt/myenv/bin/activate
export PYTHONPATH=/home/tarun/projects/MysiteGitRepo/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings2
export HOST_NAME=http://127.0.0.1/
/home/tarun/projects/MysiteGitRepo/myenv/bin/gunicorn -c /home/tarun/projects/MysiteGitRepo/MySite/scripts/gunicorn.py mysite.wsgi --reload

/home/tarun/projects/MysiteGitRepo/myenv/bin/gunicorn  mysite.wsgi:application -b 127.0.0.1:8000

source /var/www/appzcentre.com/djenv/bin/activate
export PYTHONPATH=/var/www/appzcentre.com/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://45.55.185.30/
/var/www/appzcentre.com/djenv/bin/gunicorn -c /var/www/appzcentre.com/MySite/scripts/gunicorn.py mysite.wsgi --reload

nohup /var/www/appzcentre.com/djenv/bin/gunicorn -c /var/www/appzcentre.com/MySite/scripts/gunicorn.py mysite.wsgi --reload  > /dev/null 2>&1&

gunicorn --bind appzcentre.com:8001 mysite.wsgi:application

source /var/www/djenv/bin/activate
export PYTHONPATH=/var/www/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://128.199.185.127/
/var/www/djenv/bin/gunicorn -c /var/www/MySite/scripts/gunicorn.py mysite.wsgi --reload

nohup /var/www/djenv/bin/gunicorn -c /var/www/MySite/scripts/gunicorn.py mysite.wsgi --reload > /dev/null 2>&1&



source /var/www/djenv/bin/activate
export PYTHONPATH=/var/www/old/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://128.199.185.127/
nohup /var/www/djenv/bin/gunicorn -c /var/www/old/MySite/scripts/gunicorn.py mysite.wsgi --reload > /dev/null 2>&1&


python manage.py runserver appzcentre.com:8000


 $.ajax({ // create an AJAX call...
                        data: $(this).serialize(), // get the form data
                        type: $(this).attr('method'), // GET or POST
                        url: $(this).attr('action'), // the file to call
                        success: function(response) { // on success..
                        result = JSON.parse(response);
                        $('#detail').hide();
                        $('#result').show();
                        $('#result').html(result);
                         // update the DIV
                         },
                        error: function(e, x, r) { // on error..
                        //$('#error_div).html(e); // update the DIV
                        }
                    });


 e.preventDefault();
                    url=$(this).attr('action')
                    $.post(url, function(data){
                        $('#detail').hide();
                        $('#result').show();
                        $('#result').html(data);
                    });

<script type="text/javascript">

                    var base_url = 'http://'+window.location.hostname;
                    //$('#result').hide();


                   $(document).ready(function(e) {

                    $('#form_vote').submit(function() { // catch the form's submit event
                     $.ajax({ // create an AJAX call...
                        data: $(this).serialize(), // get the form data
                        type: $(this).attr('method'), // GET or POST
                        url: $(this).attr('action'), // the file to call
                        success: function(data) { // on success..
                        //result = JSON.parse(data);
                        var html = $(data).filter('#result').html();
                        //$('#detail').hide();

                        //$('#result').show();

                        $('#result').html(html);
                         // update the DIV
                         },
                        error: function(e, x, r) { // on error..
                        //$('#error_div).html(e); // update the DIV
                        }
                    });
                    e.preventDefault();
                    return false;
    });

});
         </script>
