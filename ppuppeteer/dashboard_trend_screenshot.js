const puppeteer = require('puppeteer');
const https = require('https');
const http = require('http');

const searchable = process.argv.includes('--searchable');

const avisoURL = 'http://localhost:8090';

(async() => {
    // const browser = await puppeteer.launch({headless: false,
    //                                         slowMo: 100});
    const browser = await puppeteer.launch();

    // const browser = await puppeteer.launch({headless: false});

    const page = await browser.newPage();
    await page.setViewport({width: 1200, height: 800, deviceScaleFactor: 2});
    await page.goto(avisoURL);
    // Taking screen shot of welcome page
    await page.screenshot({path: 'sign_in.png'});

    // Inserting username into username field
    await page.type('#username', process.env.AVISO_USER);
    await page.click('.submitbtn');

    // Waiting on appearance of SIGN IN button that is disabled
    // had to do this as no new selector is being added or not page load is happening
    // Type password
    await page.waitForSelector('.signinnext .button.submitbtn.disabled', {visible: true});
    await page.type('#login_password', process.env.AVISO_PWD);
    await page.waitForSelector('.button.submitbtn.valid');
    await page.screenshot({ path: 'password_page.png' });

    // await page.evaluate(() => document.querySelector('div.outter-loginbox.show  button.button.submitbtn.valid').click());
    // Login and take screen shot of homepage
    await page.click('div.outter-loginbox.show  button.button.submitbtn.valid');
    await page.waitForNavigation();
    await page.screenshot({path: 'home.png'});

    // Logged in now switch take screen shot of forecast
    await page.select('#tenant_list', 'ooyala_test.com');
    await page.waitForNavigation();
    // await page.waitForSelector('.main-container', {visible: true});
    // await page.waitForSelector('.spinning-loader-overlay', {visible: false});
    await page.waitForSelector('.fm-grid-wrapper', {visible: true});
    await page.waitForSelector('.spinning-loader-overlay', {hidden: true });
    await page.screenshot({path: 'forecast.png'});

    const only_forecast = await page.$('.main-container');
    await only_forecast.screenshot({path: 'only_forecast.png'});


    // now lets switch to dashboard and take picture of trend graph
    await page.click('.fa.fa-tachometer');
    await page.waitForNavigation();
    await page.waitForSelector('.trend', {visible: true});
    // await page.setViewport({width: 1200, height: 800, deviceScaleFactor: 2});
    // await page.setViewport({width: 1200, height: 800});

    // await page.waitFor(3000);
    const trend = await page.$('.trend');
    await trend.screenshot({path: 'trend.png'});

    await http.get(avisoURL + '/userslist', (resp) => {
        let data = '';
        console.log('Got response: in userslist in async' + resp.statusCode);

    }).on('error', (err) => {
        console.log('Error: ' + err.message);
    });
    
    get_user_hierarchies();

    await browser.close();
}
)();

function get_csrf_token() {
    return new Promise((resolve, reject) => {
        http.get(avisoURL + '/csrfform', (resp) => {
            // console.log('From CSRFform');
            let data = '';
            // console.log('Got response: ' + resp.statusCode);
            resp.on('data', chunk => {
                // console.log('BODY: ' + chunk);
                // chunk = JSON.stringify(chunk);
                chunk = '' + chunk;
                // console.log(`after stringify ${chunk}`);
                const string_parts = chunk.split("'");
                // console.log(string_parts);
                csrf_token = string_parts[string_parts.length - 2];
                resolve(csrf_token);
                // return csrf_token;
                // console.log(`csrf_token ${csrf_token}`);
            });
        }).on('error', (err) => {
            console.log('Error: ' + err.message);
            reject(err.message);
        });
    });
    
}

function get_user_hierarchies() {
    const get_csrf_token_prom = get_csrf_token();

    get_csrf_token_prom.then(csrf_token => {
        console.log(`inside get_user_hierarchies ${csrf_token}`);
        var options = {
            hostname: 'localhost',
            // port: '8090',
            port: '5000',
            // path: '/account/login',
            path: '/',
            method: 'POST',
            headers: {'X-CSRFToken': csrf_token,
                      REFERER: 'http://localhost:8090'}
        };

        console.log(`value in options ${options.headers['X-CSRFToken']}`);
        console.log(`value in options ${JSON.stringify(options)}`);

        const data = JSON.stringify ({
            username: process.env.AVISO_USER,
            password: process.env.AVISO_PWD
        });

        console.log(`csrf in data ${data} ${csrf_token}`);
        const req = http.request(options, (res) => {
            console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
            console.log(`statusCode in login: ${res.statusCode}`);

            res.on('data', (d) => {
                process.stdout.write(d);
            });
            
        });

        req.write(data);
        req.end();
    });
    
    http.get(avisoURL + '/access/login', (resp) => {
        let data = '';
        console.log('Got response: ' + resp.statusCode);

    }).on('error', (err) => {
        console.log('Error: ' + err.message);
    });
    
    http.get(avisoURL + '/userslist', (resp) => {
        let data = '';
        console.log('Got response: in userslist ' + resp.statusCode);

    }).on('error', (err) => {
        console.log('Error: ' + err.message);
    });
}


get_user_hierarchies();
