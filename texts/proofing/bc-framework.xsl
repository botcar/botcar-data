<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:cts="http://chs.harvard.edu/xmlns/cts3" xmlns:dc="http://purl.org/dc/elements/1.1" xmlns:tei="http://www.tei-c.org/ns/1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:include href="bc-elements.xsl"/>
	<!-- Framework for main body of document -->
	<xsl:template match="/">
		
	    
		<html>
			<head>
				<title><xsl:value-of select="//tei:title"/>
					
				</title>
			    <link href='http://fonts.googleapis.com/css?family=IM+Fell+DW+Pica:400,400italic' rel='stylesheet' type='text/css'/>
			    <link href='http://fonts.googleapis.com/css?family=Italianno' rel='stylesheet' type='text/css'/>
			    <link href="proofing/normalize.css" rel="stylesheet" title="CSS for CTS" type="text/css"/>
			    <link href="proofing/bc.css" rel="stylesheet" title="CSS for CTS" type="text/css"/>
			</head>
			<body>
				<header>
					
				</header>
				<article>
				    <div class="bc_notice">
				        <p>This is a work-in-progress. It is an incomplete text, undergoing further transcription, 
				            editing, and proofing. We post it here for our own use only. The writings of the 18th Century naturalists is in 
				            the Public Domain. This edition—the semantic and descriptive markup of the XML text 
				            and the stylesheets that render that XML for display in HTML, are licensed under a 
				            Creative Commons Attribution-NonCommercial 3.0 Unported License.</p>
				        <p>2012. Amy Hackney Blackwell &amp; Christopher Blackwell. 
				        	<a href="http://folio.furman.edu/botcar"><i>Botanica Caroliniana,</i> 
				        	Interdisciplinary Research in Historical Botany. Department of Classics, Furman University.</a></p>
				    	<p>This presentation is intended as a demonstration. The completed text will be published as XML source, with these stylesheets, and for automated discovery and retrieval by canonical citation through the <a href="http://www.homermultitext.org/hmt-doc/cite/index.html">Canonical Text Services Protocol.</a></p>
				    </div>
				    
                    <xsl:apply-templates select="//tei:titleStmt"/>
				    <xsl:apply-templates select="//tei:publicationStmt"/>
					<xsl:apply-templates select="//tei:text/tei:body/*"/>
				</article>
				<footer>
					
				</footer>
			</body>
		</html>
	</xsl:template>
	<!-- End Framework for main body document -->
	<!-- Match elements of the CTS reply -->
	<xsl:template match="tei:text">
		
			<xsl:apply-templates/>
		
	</xsl:template>

	
	<!-- Default: replicate unrecognized markup -->
	<xsl:template match="@*|node()" priority="-1">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()"/>
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
