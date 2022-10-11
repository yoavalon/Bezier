d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,1)

d.end()
