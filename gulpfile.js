var gulp = require('gulp');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var concat = require('gulp-concat');

gulp.task('default', function() {
    var DEST_DIR = 'build';
    var CONCAT_FILE_NAME = 'all';

    gulp.src([
        'bower_components/underscore/underscore.js',
        'bower_components/jquery/dist/jquery.js',
        'bower_components/bootstrap/dist/js/bootstrap.js',
        'bower_components/jasny-bootstrap/dist/js/jasny-bootstrap.js'
    ])
      .pipe(uglify())
      .pipe(concat(CONCAT_FILE_NAME + '.js'))
      .pipe(gulp.dest(DEST_DIR));

    gulp.src([
        'bower_components/bootstrap/dist/css/bootstrap.css',
        'bower_components/jasny-bootstrap/dist/css/jasny-bootstrap.css',
    ])
      .pipe(minifyCSS())
      .pipe(concat(CONCAT_FILE_NAME + '.css'))
      .pipe(gulp.dest(DEST_DIR));

    gulp.src('bower_components/bootstrap/dist/fonts/*').pipe(gulp.dest(DEST_DIR + '/fonts'));
});