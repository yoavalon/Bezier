d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,3)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
