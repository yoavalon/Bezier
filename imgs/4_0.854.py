d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,0)

d.end()
