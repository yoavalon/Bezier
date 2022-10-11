d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
