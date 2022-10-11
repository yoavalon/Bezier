d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.N, Length.long)
d.position_pen(1,2)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
