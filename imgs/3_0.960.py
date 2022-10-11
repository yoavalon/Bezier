d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)

d.end()
