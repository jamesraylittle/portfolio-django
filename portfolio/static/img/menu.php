            <!-- MENU -->
            <div class="nav-collapse nav-collapse_  collapse">
              <ul class="nav sf-menu">
            <?php
				$pages = array("Home", "Projects", "About Me", "Resume", "Contact");
				foreach($pages as $file){
					$filename = strtolower(str_replace(" ", "_", $file));
					$li = '<li>';
					if($page == $filename)
						$li = '<li class="active">';
					echo $li.'<a href="?page='.$filename.'">'.$file.'</a></li>';
				}
			?>
              <!--  <li><a href="?page=home">Home</a></li>
                <li><a href="?page=projects">Projects</a></li>
                <li><a href="?page=about_me">About Me</a></li>
                <li><a href="?page=resume">Resume</a></li>
                <li><a href="?page=contact">Contact</a></li> -->
              </ul> 
            </div>
            
            
<?php
//I didn't want this to show up in the HTML source, but below is how to have a sub-menu using this template
/*
               <li class="sub-menu"><a href="process.html">Process</a>
                  <ul>
                    <li><a href="#">Process 01</a></li>
                    <li><a href="#">Process 02</a></li>
                    <li><a href="#">Process 03</a></li>
                  </ul>
               </li>
*/
?>