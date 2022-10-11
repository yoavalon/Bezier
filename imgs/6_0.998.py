d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.short)

d.end()
