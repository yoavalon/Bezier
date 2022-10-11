d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)

d.end()
