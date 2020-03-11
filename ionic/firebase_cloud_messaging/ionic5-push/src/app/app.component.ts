import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { Router } from '@angular/router'

import { FCM } from '@ionic-native/fcm/ngx'

import { from } from 'rxjs';

@Component({
    selector: 'app-root',
    templateUrl: 'app.component.html',
    styleUrls: ['app.component.scss']
})
export class AppComponent {
    constructor(
        private platform: Platform,
        private splashScreen: SplashScreen,
        private statusBar: StatusBar,
        private fcm: FCM,
        private router: Router
    ) {
        this.initializeApp();
    }

    initializeApp() {
        this.platform.ready().then(() => {
            this.statusBar.styleDefault();
            this.splashScreen.hide();
            this.fcm.getToken().then(token => {
                console.log('ironman ' + token)
            })

            this.fcm.onTokenRefresh().subscribe(token => {
                console.log('ironman refresh ' + token);
            });

            this.fcm.onNotification().subscribe(data => {
                console.log(data);
                if (data.wasTapped) {
                    console.log('Received in background');
                    this.router.navigate([data.landing_page, data.price]);
                } else {
                    console.log('Received in foreground');
                    this.router.navigate([data.landing_page, data.price]);
                }
            });
        });
    }
}
