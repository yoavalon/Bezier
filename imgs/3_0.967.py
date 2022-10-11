d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,3)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,2)

d.end()
