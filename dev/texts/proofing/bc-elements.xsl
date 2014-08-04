<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:cts="http://chs.harvard.edu/xmlns/cts3" xmlns:dc="http://purl.org/dc/elements/1.1" xmlns:tei="http://www.tei-c.org/ns/1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<!-- ********************************************************** -->
	<!-- Include support for a handful of TEI namespaced elements   -->
	<!-- ********************************************************** -->
    <!-- Botanica Caroliniana -->
    
    <xsl:variable name="imgsvc-thumb-url">http://amphoreus.hpcc.uh.edu/tomcat/chsimg/Img?request=GetBinaryImage&amp;w=1000&amp;urn=</xsl:variable>
    <xsl:variable name="imgsvc-zoom-url">http://amphoreus.hpcc.uh.edu/tomcat/chsimg/Img?request=GetIIPMooViewer&amp;urn=</xsl:variable>
    <xsl:variable name="gip-url">http://folio.furman.edu/citeimg/</xsl:variable>
    
 	<xsl:template match="tei:p[@n='H']">
 		<h2><xsl:apply-templates/></h2>
 	</xsl:template>
 
    <xsl:template match="tei:titleStmt">
        <xsl:apply-templates/>
    </xsl:template>
 
    <xsl:template match="tei:title[@type='full']">
        <xsl:element name="div">
            <xsl:attribute name="class">
                <xsl:if test="@xml:lang = 'fr'"> bc_fra_column</xsl:if>
                <xsl:if test="@xml:lang = 'en'"> bc_eng_column</xsl:if>
            </xsl:attribute>
            
            <xsl:apply-templates/>
            
        </xsl:element>
        <xsl:if test="@xml:lang = 'fr'"><div class="bc_clear"> </div></xsl:if>
    </xsl:template>
    
    <xsl:template match="tei:author">
        <p class="bc_author"><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="tei:hi[@rend='italics']">
        <em><xsl:apply-templates/></em>
    </xsl:template>
    
    <xsl:template match="tei:title[@level = 'm']">
        <span class="bc_worktitle"><xsl:apply-templates/></span>
    </xsl:template>
    
    <xsl:template match="tei:title">
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    
    
    <xsl:template match="tei:publicationStmt">
        <div class="bc_publicationStmt">
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="tei:note">
        <div class="bc_marginalNote"><xsl:apply-templates/></div>
    </xsl:template>
 
    <xsl:template match="tei:p">
        <xsl:element name="p">
            <xsl:attribute name="class">
                <xsl:if test="@xml:lang = 'fr'"> bc_french</xsl:if>
                <xsl:if test="@xml:lang = 'la'"> bc_latin</xsl:if>
                <xsl:if test="@xml:lang = 'en'"> bc_english</xsl:if>
            </xsl:attribute>
            <xsl:if test="@n">
                <span class="bc_citation"><xsl:if test="../../../@n"><xsl:value-of select="../../../@n"/>.</xsl:if><xsl:value-of select="../../@n"/>.<xsl:value-of select="../@n"/>.<xsl:value-of select="@n"/></span>
            </xsl:if>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
 
 	<xsl:template match="tei:div">
 		<xsl:element name="div">
 			<xsl:attribute name="class">
 				<xsl:if test="@xml:lang = 'fr'"> bc_french</xsl:if>
 				<xsl:if test="@xml:lang = 'la'"> bc_latin</xsl:if>
 				<xsl:if test="@xml:lang = 'en'"> bc_english</xsl:if>
 			    <xsl:if test="@n = 'Eng'"> bc_eng_column</xsl:if>
 			    <xsl:if test="@n = 'Fra'"> bc_fra_column</xsl:if>
 			    <xsl:if test="@type = 'section'"> bc_section</xsl:if>
 			</xsl:attribute>
 		    
 			<xsl:apply-templates/>
 		    
 		</xsl:element>
 	    <xsl:if test="@n = 'Fra'"><div class="bc_clear"> </div></xsl:if>
 	
 	</xsl:template>
 
 
 <xsl:template match="tei:figDesc">
     <xsl:element name="div">
         <xsl:attribute name="class">bc_figure</xsl:attribute>
         <p class="bc_figure_instructions">
             <xsl:element name="a">
                 <xsl:attribute name="href"><xsl:value-of select="$imgsvc-zoom-url"/><xsl:value-of select="@facs"/></xsl:attribute>
                 Link to dynamic view.
             </xsl:element>
             
             <xsl:element name="a">
                 <xsl:attribute name="href"><xsl:value-of select="$gip-url"/><xsl:value-of select="@facs"/></xsl:attribute>
                 Link to image, metadata, &amp; citation tool.
             </xsl:element>
         </p>
         <xsl:element name="a">
             <xsl:attribute name="href"><xsl:value-of select="$imgsvc-zoom-url"/><xsl:value-of select="@facs"/></xsl:attribute>
            <xsl:element name="img">
              <xsl:attribute name="w">1000</xsl:attribute>
              <xsl:attribute name="src"><xsl:value-of select="$imgsvc-thumb-url"/><xsl:value-of select="@facs"/></xsl:attribute>
            </xsl:element>
         </xsl:element>
        <xsl:apply-templates/>
         <div class="bc_clear"> </div>
     </xsl:element>
 </xsl:template>


    <xsl:template match="tei:ref">
        <xsl:element name="div">
            <xsl:attribute name="class">
                
                bc_ref
            </xsl:attribute>
            
            <xsl:apply-templates/>
            
        </xsl:element>
    </xsl:template>
    
    
    <xsl:template match="tei:caption">
        <xsl:element name="div">
            <xsl:attribute name="class">
                <xsl:if test="@xml:lang = 'fr'"> bc_french</xsl:if>
                <xsl:if test="@xml:lang = 'la'"> bc_latin</xsl:if>
                <xsl:if test="@xml:lang = 'en'"> bc_english</xsl:if>
            
            </xsl:attribute>
            
            <xsl:apply-templates/>
            
        </xsl:element>
    </xsl:template>
 
 <xsl:template match="tei:emph">
 	<em><xsl:apply-templates/></em>
 </xsl:template>
</xsl:stylesheet>
