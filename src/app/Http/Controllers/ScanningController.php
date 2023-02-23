<?php

namespace App\Http\Controllers;
use Predis\Client;
use Illuminate\Http\Request;

class ScanningController extends Controller
{
    public function handleForm(Request $request)
    {
        // Récupérer les données du formulaire
        $url = $request->input('url');
        //dd($url);
        // Ajouter à une file d'attente Redis
       $redis = new Client([
            'scheme' => 'tcp',
            'host' => 'redis',
            'port' => 6379,
        ]);

        $redis->rpush('urls-to-scan', $url);
        // Rediriger l'utilisateur vers une autre page*/
        return redirect()->back();
    }

    public function storeWebsites(){}
}
