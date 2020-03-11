import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
    // { path: '', redirectTo: 'home', pathMatch: 'full' },
    // { path: 'home', loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)},
    // {
    //     path: 'movies',
    //     loadChildren: () => import('./pages/movies/movies.module').then(m => m.MoviesPageModule)
    // },
    // {
    //     path: 'movie-details',
    //     loadChildren: () => import('./pages/movie-details/movie-details.module').then(m => m.MovieDetailsPageModule)
    // },
    { path: '', redirectTo: 'movies', pathMatch: 'full' },
    { path: 'movies', loadChildren: './pages/movies/movies.module#MoviesPageModule' },
    { path: 'movies/:id', loadChildren: './pages/movie-details/movie-details.module#MovieDetailsPageModule' }
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
    ],
    exports: [RouterModule]
})
export class AppRoutingModule { }
