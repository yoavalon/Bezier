d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,0)

d.end()
